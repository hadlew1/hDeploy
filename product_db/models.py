from django.db import models
from django_enumfield import enum

class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.TextField()
    stock_qty = models.IntegerField()
class supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.TextField()
    supplier_address= models.TextField()
class purchase_order(models.Model):
    purchase_order_id=models.AutoField(primary_key=True)
    supplier_id = models.ForeignKey(supplier,on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)
#using bridge table to make many products on many orders possible
class product_purchase_order(models.Model):
    product_id=models.ForeignKey(product, on_delete = models.CASCADE)
    purchase_order_id=models.ForeignKey(purchase_order, on_delete = models.CASCADE)
    quantity = models.IntegerField()



