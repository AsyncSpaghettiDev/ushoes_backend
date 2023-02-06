# import coupon models
from .models import Coupon

# import coupon serializers
from .serializers import CouponSerializer
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from django.http.response import HttpResponseBadRequest, HttpResponseNotFound
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import exception_handler

# Create your views here.


class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request):
        queryset = Coupon.objects.all()
        serializer = CouponSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Coupon.objects.all()
        try:
            coupon = get_object_or_404(queryset, pk=pk)
        except ValueError:
            return HttpResponseBadRequest("Invalid coupon id")

        serializer = CouponSerializer(coupon)
        return Response(serializer.data)

    def create(self, request):
        serializer = CouponSerializer(data=request.data)
        # check if the coupon code already exists
        if Coupon.objects.filter(code=request.data['code']).exists():
            return HttpResponseBadRequest("Coupon code already exists")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk=None):
        coupon = Coupon.objects.get(pk=pk)
        serializer = CouponSerializer(coupon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        coupon = Coupon.objects.get(pk=pk)
        # don't delete the coupon, just set the remaining to 0 or active to false
        coupon.remaining = 0
        coupon.active = False
        coupon.save()
        return Response('Coupon deleted.')

    @action(detail=False, methods=['post'], url_name='redeem', url_path='redeem')
    def redeem(self, request):
        try:
            code = request.data['code']
        except KeyError:
            return HttpResponseBadRequest("Invalid coupon code")

        coupon = Coupon.objects.get(code=code)
        if coupon.remaining > 0:
            coupon.remaining -= 1
            coupon.save()
            return Response({'discount': coupon.discount})
        else:
            return HttpResponseBadRequest("Coupon expired or invalid")
