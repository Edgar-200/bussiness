from django.db import models




class Shipment(models.Model):
    shipment_id=models.AutoField(primary_key=True)
    shipment_date = models.DateTimeField()
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=100)
    customer=models.ForeignKey("Custom" ,on_delete=models.CASCADE)




class Custom(models.Model):
    custom_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20, unique=True, blank=False)
    address = models.CharField(max_length=100)
    phone_number=models.CharField(max_length=20)



    def __str__(self):
        return f"{self.first_name} {self.last_name}"






class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    order_date=models.DateTimeField()
    total_price=models.DecimalField(max_digits=10, decimal_places=2)

    customer = models.ForeignKey("Custom", on_delete=models.CASCADE)
    payment = models.ForeignKey("Payment", on_delete=models.CASCADE)
    ship_ment= models.ForeignKey("Shipment", on_delete=models.CASCADE)



class Order_item(models.Model):
    order_item_id=models.AutoField(primary_key=True)
    quality=models.IntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2)

    order= models.ForeignKey("Order", on_delete=models.CASCADE)



class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    description=models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock =models.IntegerField()
    category=models.ForeignKey('Category', on_delete=models.CASCADE)


    def __str__(self):
        return self.description


class Category(models.Model):
    category_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)


    def __str__(self):
        return self.name





class Payment(models.Model):
    payment_id=models.AutoField(primary_key=True)
    payment_date=models.DateTimeField()
    payment_method=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=10, decimal_places=2)

    customer = models.ForeignKey("Custom", on_delete=models.CASCADE)







class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    quality = models.IntegerField()

    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)



class Wishlist(models.Model):
     wishlist_id= models.AutoField(primary_key=True)

     category = models.ForeignKey('Category', on_delete=models.CASCADE)
     product = models.ForeignKey('Product', on_delete=models.CASCADE)

