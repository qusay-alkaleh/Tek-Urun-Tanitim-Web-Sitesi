from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from  rest_framework import generics
from rest_framework import mixins

class products(generics.ListCreateAPIView
                 ):
    
    queryset=Product.objects.all()
    serializer_class=ProductSerializer



class product_detail(
     generics.RetrieveUpdateDestroyAPIView

):
    
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


   
    











