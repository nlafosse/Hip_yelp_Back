from django.db import models
from django.contrib.postgres.fields import ArrayField

class Food(models.Model):
  name = models.CharField(max_length=100)
  group = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  photo_url = models.CharField(max_length=200)
  lat = models.CharField(max_length=20)
  lon = models.CharField(max_length=20)
  tags = tags = ArrayField(models.CharField(max_length=100), null=True, blank=True)

class Drink(models.Model):
  name = models.CharField(max_length=100)
  group = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  photo_url = models.CharField(max_length=200)
  lat = models.CharField(max_length=20)
  lon = models.CharField(max_length=20)
  tags = ArrayField(models.CharField(max_length=100), null=True, blank=True)