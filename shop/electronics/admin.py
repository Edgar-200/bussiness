from django.contrib import admin
from .models import Category,Payment,Product,Shipment,Custom,Wishlist,Cart,Order,Order_item


admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Payment)
admin.site.register(Shipment)
admin.site.register(Custom)
admin.site.register(Order)
admin.site.register(Order_item)
admin.site.register(Wishlist)

# Register your models here.
