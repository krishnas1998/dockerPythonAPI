from django.db import models

class Container(models.Model):
    name = models.CharField(max_length=64)
    image = models.CharField(max_length=64)
    labels = models.CharField(max_length=64)
    status = models.CharField(max_length=64)
