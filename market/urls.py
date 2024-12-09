from django.urls import path
from .views import CategoryViewSet,BrandViewSet

from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet,BrandViewSet

router = DefaultRouter()
router.register(r'brand', BrandViewSet, basename='brand')
router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = router.urls


