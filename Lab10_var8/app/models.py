from django.db import models


class Dogs(models.Model):
    weight = models.DecimalField(max_digits=99999,decimal_places=2,default=0)
    height = models.DecimalField(max_digits=99999,decimal_places=2,default=0)
    classification = models.CharField(max_length=225,default='')
    sound = models.CharField(max_length=225,default='')
    food = models.CharField(max_length=225,default='')
    name = models.CharField(max_length=225,default='')
    age = models.IntegerField(default=0)
