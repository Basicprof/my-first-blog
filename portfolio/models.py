from django.db import models

class Portfolio(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    url = models.CharField(max_length=200, blank=True)
