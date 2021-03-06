#https://www.django-rest-framework.org/api-guide/generic-views/
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
class productList(generics.ListCreateAPIView):
    queryset = product.objects.all()
    serializer_class = productSerializer
class productDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = product.objects.all()
    serializer_class = productSerializer
