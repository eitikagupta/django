from django.db import models

# Create your models here.
class teststu(models.Model):
    name = models.CharField(max_length=255,default="")
    phone = models.IntegerField(default=0)

class mytab(models.Model):
    name = models.CharField(max_length=255)
    age  = models.IntegerField()
    address = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=200)

class Subcategory(models.Model):
    scname = models.CharField(max_length=200)
    cid = models.ForeignKey(Category,on_delete=models.CASCADE)