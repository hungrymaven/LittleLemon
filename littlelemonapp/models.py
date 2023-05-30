from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length = 100)
    cuisine = models.CharField(max_length = 100)
    price = models.IntegerField

# class Customer(models.Model):
#     name = models.CharField(max_length=200)
#     reservation_day = models.CharField(max_length=20)
#     seats = models.IntegerField()

#     def __str__(self):
#         return self.name

class Person(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    date=models.DateField()


class MyForm(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    date=models.DateField()