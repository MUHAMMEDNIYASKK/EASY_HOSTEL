from django.db import models

# Create your models here.
class book(models.Model):
    Hid = models.IntegerField(default=0)
    Sid = models.IntegerField(default=0)
    sfn = models.CharField(max_length=50,default='')
    sln =models.CharField(max_length=50,default='')
    bdate = models.CharField(max_length=20)
    status = models.CharField(max_length=30, default='')

class attendance(models.Model):
    stid = models.CharField(max_length=6)
    date = models.CharField(max_length=20)
    status = models.CharField(max_length=30)

