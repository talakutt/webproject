from django.db import models

# Create your models here.

class Address(models.Model):
    city = models.CharField(max_length= 40)
    def __str__(self):
        return self.city
class Student(models.Model):
    name = models.CharField(max_length= 40)
    age = models.IntegerField(default= 0)
    address = models.ForeignKey(Address, on_delete = models.PROTECT)

class Teacher(models.Model):
    name = models.CharField(max_length= 20)
    photo = models.ImageField(upload_to= 'prof_pics')

    def __str__(self):
        return self.name