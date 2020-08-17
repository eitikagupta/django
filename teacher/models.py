from django.db import models

# Create your models here.
class Cat(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=244)

class Subcat4(models.Model):
    scid = models.AutoField(primary_key=True)
    cid  = models.ForeignKey(Cat,to_field='cid',on_delete=models.CASCADE)
    scname = models.CharField(max_length=255)
