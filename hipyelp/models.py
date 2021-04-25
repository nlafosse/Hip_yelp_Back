from django.db import models

class Food(models.Model):
  name = models.CharField(max_length=100)
  group = models.CharField(max_length=100, default='groups')
  address = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  photo_url = models.CharField(max_length=200, null=True)
  lon = models.CharField(max_length=20, default='lon')
  lat = models.CharField(max_length=20, default='lat')


class Drink(models.Model):
  name = models.CharField(max_length=100)
  group = models.CharField(max_length=100, default='groups')
  address = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  photo_url = models.CharField(max_length=200, null=True)
  lon = models.CharField(max_length=20, default='lon')
  lat = models.CharField(max_length=20, default='lat')

class HotSpotTag(models.Model):
  foodName = models.ManyToManyField(
    Food,
    related_name='tags',
    related_query_name='tag',
  )
  tagName = models.TextField()