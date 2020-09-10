from django.db import models


# Create your models here.
class Product(models.Model):
        name = models.CharField(max_length=50)
        price = models.IntegerField(default=0)
        description = models.CharField(max_length=20)
        image = models. ImageField(upload_to="uploads/products/")
