from django.db import models

class Ftag(models.Model):
  tags = models.CharField(max_length=20)

class Food(models.Model):
  name = models.CharField(max_length=100)
  group = models.CharField(max_length=100, default='groups')
  address = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  photo_url = models.CharField(max_length=200, null=True)
  lon = models.CharField(max_length=20, default='lon')
  lat = models.CharField(max_length=20, default='lat')
  tags = models.ManyToManyField(Ftag, related_name='foods',blank=True)

class FoodTag(models.Model):
  test = models.CharField(max_length=100, default='')
  tags = models.ForeignKey(Food, related_name='foods', on_delete=models.CASCADE, default='')

class Dtag(models.Model):
  tags = models.CharField(max_length=20)

class Drink(models.Model):
  name = models.CharField(max_length=100)
  group = models.CharField(max_length=100, default='groups')
  address = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  photo_url = models.CharField(max_length=200, null=True)
  lon = models.CharField(max_length=20, default='lon')
  lat = models.CharField(max_length=20, default='lat')
  tags = models.ManyToManyField(Ftag, related_name='drinks',blank=True)
  # tags = models.CharField(DrinkTag, max_length=50)

class DrinkTag(models.Model):
  test = models.CharField(max_length=100, default='')
  tags = models.ForeignKey(Drink, related_name='drinks', on_delete=models.CASCADE, default='')


# class DrinkTag(models.Model):
#   drinkName = models.ManyToManyField(
#     Drink,
#     related_name='drinkTags',
#     related_query_name=' drinktag',
#   )
#   tagName = models.TextField()