from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets

from .serializer import (CategorySerializer, ProductSerializer, PaymentSerializer, Order_itemSerializer,
                         OrderSerializer, WishlistSerializer, CustomSerializer, CartSerializer, ShipmentSerializer)
from .models import Category, Payment, Product, Shipment, Custom, Wishlist, Cart, Order, Order_item


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        print(self.queryset)  # Check the queryset being fetched
        return super().list(request, *args, **kwargs)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer


class Order_itemViewSet(viewsets.ModelViewSet):
    queryset = Order_item.objects.all()
    serializer_class = Order_itemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CustomViewSet(viewsets.ModelViewSet):
    queryset = Custom.objects.all()
    serializer_class = CustomSerializer


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
