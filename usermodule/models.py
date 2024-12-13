from django.db import models

# Create your models here.

class Address(models.Model):
    city = models.CharField(max_length= 40)
class Student(models.Model):
    name = models.CharField(max_length= 40)
    age = models.IntegerField(default= 0)
    address = models.ForeignKey(Address, on_delete = models.PROTECT)

