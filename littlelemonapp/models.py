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

# class Person(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.EmailField(unique=True)
#     date=models.DateField()


class Reserve(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    date=models.DateField()

class Booking(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('Phone Number', max_length=300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        indexes = models.Index(fields=['price']),
