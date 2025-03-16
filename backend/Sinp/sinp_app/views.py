from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ProductA
from .serializers import ProductSerializer


class products(generics.ListCreateAPIView):
    queryset=ProductA.objects.all()
    serializer_class=ProductSerializer


class product_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=ProductA.objects.all()
    serializer_class=ProductSerializer