from django.db import models

# Create your models here.

class Food(models.Model):
    OrderDate = models.DateField()
    Region    = models.CharField(max_length=15)
    City      = models.CharField(max_length=20)
    Category  = models.CharField(max_length=20)
    Product   = models.CharField(max_length=20)
    Quantity  = models.IntegerField()
    UnitPrice = models.DecimalField(max_digits=3, decimal_places=2)

