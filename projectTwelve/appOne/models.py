from django.db import models

# Create your models here.
class Product(models.Model):

    productBrandName = models.CharField(max_length=30)
    productBrandModel = models.CharField(max_length=30)
    productBrandCost = models.FloatField()

    
