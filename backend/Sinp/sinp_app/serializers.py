from rest_framework import serializers
from .models import ProductA

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model=ProductA
        fields="__all__"