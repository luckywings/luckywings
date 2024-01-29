from django.db import models

# Create your models here.

class Product(models.Model):
    item=models.CharField(max_length=100)
    price=models.FloatField()
    decription=models.TextField(max_length=500)
    image=models.CharField(max_length=500)
    def __str__(self):
        return self.item