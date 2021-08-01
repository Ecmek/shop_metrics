from django.db import models


class Shop(models.Model):
    date = models.DateField()
    shop = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    visitors = models.PositiveIntegerField()
    earnings = models.PositiveIntegerField()
