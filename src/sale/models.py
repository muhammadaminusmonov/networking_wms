from django.db import models
from product.models import Product


class Sale(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name.name