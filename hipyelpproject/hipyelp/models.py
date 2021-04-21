from django.db import models

# Create your models here.
class HotSpot(models.Model):
  category = models.CharField(max_length=100)

class Food(models.Model):
  category = models.ForeignKey(HotSpot, on_delete=models.CASCADE, related_name='foods')
  name = models.CharField(max_length=100, default='no restaraunt name')
  address = models.CharField(max_length=100, default='no address')
  comment = models.CharField(max_length=500, default='no comments')

class Drink(models.Model):
  category = models.ForeignKey(HotSpot, on_delete=models.CASCADE, related_name='drinks')
  name = models.CharField(max_length=100, default='no bar name')
  address = models.CharField(max_length=100, default='no address')
  comment = models.CharField(max_length=500, default='no comments')

