from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    amount = models.IntegerField()

    def __str__(self):
        return self.name