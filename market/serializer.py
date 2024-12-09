from rest_framework import serializers

from .models import Brand,Category,Products


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model= Brand
        fields='__all__'



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields='__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Products
        fields='__all__'
