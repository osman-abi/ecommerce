from django.db import models
from products.models import Product
# Create your models here.
class Favourite(models.Model):
    product = models.ManyToManyField(Product)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    