from django.db import models
from django.utils.text import slugify


class Stock(models.Model):
    name = models.CharField(max_length=100)
    currentPrice = models.IntegerField()
    lastUpdate = models.DateTimeField(auto_now=True)
    createDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
    
    