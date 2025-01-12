from rest_framework import serializers

from .models import Category,Payment,Product,Shipment,Custom,Wishlist,Cart,Order,Order_item



class CategorySerializer(serializers.Serializer):
    class Meta:
        brand = Category
        fields = "__all__"

class PaymentSerializer(serializers.Serializer):

    class Meta:
        brand = Payment
        fields = "__all__"


class ProductSerializer(serializers.Serializer):
    class Meta:
        brand = Product
        fields = "__all__"


class ShipmentSerializer(serializers.Serializer):
    class Meta:
        brand = Shipment
        fields = "__all__"


class CustomSerializer(serializers.Serializer):
    class Meta:
        brand = Custom
        fields ="__all__"



class CartSerializer(serializers.Serializer):
    class Meta:
        brand = Cart
        fields = "__all__"


class WishlistSerializer(serializers.Serializer):
    class Meta:
        brand = Wishlist
        fields = "__all__"


class Order_itemSerializer(serializers.Serializer):
    class Meta:
        brand = Order_item
        fields = "__all__"


class OrderSerializer(serializers.Serializer):
    class Meta:
        brand = Order
        fields = "__all__"

