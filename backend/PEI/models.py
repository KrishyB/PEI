from pyexpat import model
from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to ='img/')
    model = models.TextField()
    price = models.IntegerField()
    brand = models.TextField(default='generic')
    inCart = models.IntegerField(default=0)

class Parameter(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    parameter = models.TextField()
    value = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
            fields=['id','parameter'],
            name= 'parameter_for_product'
        )
        ]