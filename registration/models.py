from django.db import models
from django import forms


class student(models.Model):
    studentname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=False,blank=False)

class product(models.Model):
    productname = models.CharField(max_length=100)
    categoryname = models.CharField(max_length=100)


class cars(models.Model):
    carname = models.CharField(max_length=100)
    price = models






