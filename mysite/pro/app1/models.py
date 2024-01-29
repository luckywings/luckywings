from django.db import models

# Create your models here.
class student(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=25)
    place=models.CharField(max_length=25)