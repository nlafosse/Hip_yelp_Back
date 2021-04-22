from django.db import models

class Food(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  description = models.CharField(max_length=500)

class Drink(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  description = models.CharField(max_length=500)