from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    no=models.IntegerField()
    city=models.CharField(max_length=50)