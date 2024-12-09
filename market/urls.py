from django.urls import path
from .views import CategoryViewSet,BrandViewSet,ProductsViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'brand', BrandViewSet, basename='brand')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductsViewSet, basename='Product')


urlpatterns = router.urls


