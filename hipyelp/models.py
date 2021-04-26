from django.db import models

class Food(models.Model):
  name = models.CharField(max_length=100)
  group = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  photo_url = models.CharField(max_length=200)
  lat = models.CharField(max_length=20)
  lon = models.CharField(max_length=20)

class Drink(models.Model):
  name = models.CharField(max_length=100)
  group = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  photo_url = models.CharField(max_length=200)
  lat = models.CharField(max_length=20)
  lon = models.CharField(max_length=20)

class FoodTag(models.Model):
  foodName = models.ManyToManyField(
    Food,
    related_name='foodTags',
    related_query_name='foodtag',
  )
  tags = models.CharField(max_length=20)

class DrinkTag(models.Model):
  drinkName = models.ManyToManyField(
    Drink,
    related_name='drinkTags',
    related_query_name=' drinktag',
  )
  tags = models.CharField(max_length=20)