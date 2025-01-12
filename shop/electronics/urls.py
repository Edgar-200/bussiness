from django.urls import path

from .views import (CategoryViewSet,CartViewSet,ProductViewSet,PaymentViewSet,WishlistViewSet
                                                ,CustomViewSet,OrderViewSet,Order_itemViewSet)

from rest_framework .routers import DefaultRouter

route = DefaultRouter()
route.register(r"category" ,CategoryViewSet ,basename='category')
route.register(r"cart", CartViewSet ,basename='cart')
route.register(r"custom", CustomViewSet ,basename='custom')
route.register(r"product",ProductViewSet ,basename='product')
route.register(r"Payment", PaymentViewSet ,basename='payment')
route.register(r"order_item", Order_itemViewSet ,basename='order_item')
route.register(r"order", OrderViewSet,basename='order')
route.register(r"wishlist", WishlistViewSet ,basename='wishlist')


urlpatterns = route.urls

