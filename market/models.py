from django.db import models
from mptt.models import TreeForeignKey,MPTTModel


class Category(MPTTModel):
    name =models.CharField(max_length=100)
    parent=TreeForeignKey("self", on_delete=models.CASCADE)


class MTTPMeta:
    order_insertion_by=['name']



    def __str__(self):
         return self.name





class Brand(models.Model):

    name= models.CharField(max_length=100)
    description = models.TextField(blank=True)



    def __str__(self):
     return self.name

class Products(models.Model):

    name= models.CharField(max_length=100)
    description=models.TextField(blank=True)
    type=models.BooleanField(blank=True,null=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    category=TreeForeignKey("category",on_delete=models.CASCADE)


    def __str__(self):
        return self.name