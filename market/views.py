from django.shortcuts import render


from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import CategorySerializer,ProductSerializer,BrandSerializer
from .models import Category,Products,Brand


class CategoryViewSet(viewsets.ViewSet):
    """
    view of viewing category viewsets
    """
    querySet=Category.objects.all()



    def list(self,request):
        serializer=CategorySerializer(self.querySet, many=True)
        return Response (serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
     view of viewing brand viewsets
     """
    querySet=Brand.objects.all()


    def list(self,request):
        serializer=BrandSerializer(self.querySet , many=True)
        return Response(serializer.data)


class ProductsViewSet(viewsets.ViewSet):
    """
        view of viewing product viewsets
        """

    querySet=Products.objects.all()


    def list(self,request):
        serializer=ProductSerializer(self.querySet, many=True)
        return Response(serializer.data)


