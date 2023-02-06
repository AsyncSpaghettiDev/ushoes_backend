# import sales models
from .models import Order

# import sales serializers
from .serializers import OrderSerializer
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from django.http.response import HttpResponseBadRequest, HttpResponseNotFound
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import exception_handler

import stripe

# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Order.objects.all()
        try:
            order = get_object_or_404(queryset, pk=pk)
        except ValueError:
            return HttpResponseBadRequest("Invalid order id")

        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        if request.data['coupon'] is not None:
            coupon = Coupon.objects.filter(code=request.data['coupon']).first()
            # check if the coupon is valid, if not, return error, else, deduct the coupon
            if coupon is None:
                return HttpResponseBadRequest("Invalid coupon code")
            elif coupon.is_valid is False:
                return HttpResponseBadRequest("Coupon is not valid")
            else:
                if coupon.remaining == 1:
                    coupon.is_valid = False
                coupon.remaining -= 1
                coupon.save()

        if request.data['order_type'] == 'delivery' and request.data['address'] is None:
            return HttpResponseBadRequest("Address is required for delivery")

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk=None):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response("Order deleted")

    @action(detail=False, methods=['post'], permission_classes=[AllowAny], url_path='pay', url_name='pay')
    def pay(self, request):
        # get the order id from the request
        order = Order.objects.get(pk=request.data['order_id'])
        # check if the order is valid
        if order is None:
            return HttpResponseBadRequest("Invalid order id")
        if order.is_paid is True:
            return HttpResponseBadRequest("Order has already been paid")
