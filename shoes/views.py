# import shoe models
from .models import Shoe

# import shoe serializers
from .serializers import ShoeSerializer
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
import stripe
from environs import Env

env = Env()
env.read_env()
STRIPE_SECRET_KEY = env.str('STRIPE_SECRET_KEY')


class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request):
        queryset = Shoe.objects.all()
        serializer = ShoeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Shoe.objects.all()
        try:
            shoe = get_object_or_404(queryset, pk=pk)
        except ValueError:
            return HttpResponseBadRequest("Invalid shoe id")

        serializer = ShoeSerializer(shoe)
        return Response(serializer.data)

    def create(self, request):
        serializer = ShoeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk=None):
        shoe = Shoe.objects.get(pk=pk)
        serializer = ShoeSerializer(shoe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        shoe = Shoe.objects.get(pk=pk)
        shoe.delete()
        return Response('Shoe deleted.')

    @action(detail=False, methods=['get'], url_name='by-type', url_path='type/(?P<id>\w+)')
    def shoe_types(self, request, *args, **kwargs):
        if not "id" in kwargs or not kwargs["id"]:
            return HttpResponseBadRequest("Type is required")

        shoe_type = kwargs["id"]

        try:
            queryset = Shoe.objects.filter(shoe_type=shoe_type)
        except ValueError:
            queryset = Shoe.objects.filter(shoe_type__style=shoe_type)

        if queryset.count() == 0:
            return HttpResponseNotFound("No shoes found for this type")

        serializer = ShoeSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_name='by-gender', url_path='gender/(?P<id>\w+)')
    def shoe_gender(self, request, *args, **kwargs):
        if not "id" in kwargs or not kwargs["id"]:
            return HttpResponseBadRequest("You should specify the gender")

        shoe_gender = kwargs["id"]

        try:
            queryset = Shoe.objects.filter(gender=shoe_gender)
        except ValueError:
            queryset = Shoe.objects.filter(gender__name=shoe_gender)

        if queryset.count() == 0:
            return HttpResponseNotFound("No shoes found for this gender")

        queryset = Shoe.objects.filter(gender=shoe_gender)

    @action(detail=False, methods=['get'], url_name='by-brand', url_path='brand/(?P<id>\w+)')
    def shoe_brand(self, request, *args, **kwargs):
        if not "id" in kwargs or not kwargs["id"]:
            return HttpResponseBadRequest("You should specify the brand")

        shoe_brand = kwargs["id"]

        try:
            queryset = Shoe.objects.filter(brand=shoe_brand)
        except ValueError:
            queryset = Shoe.objects.filter(brand__name=shoe_brand)

        if queryset.count() == 0:
            return HttpResponseNotFound("No shoes found for this brand")

        queryset = Shoe.objects.filter(brand=shoe_brand)
