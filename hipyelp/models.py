from django.db import models

# class Ftag(models.Model):
#   tags = models.CharField(max_length=20)
# class Tag(models.Model):
#   tags = models.CharField(max_length=20)

class Food(models.Model):
  name = models.CharField(max_length=100)
  group = models.CharField(max_length=100, default='groups')
  address = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  photo_url = models.CharField(max_length=200, null=True)
  lat = models.CharField(max_length=20, default='lat')
  lon = models.CharField(max_length=20, default='lon')
  tags = models.CharField(max_length=20, default='tags')

# class FoodTag(models.Model):
#   foodtag = models.ForeignKey(Food, related_name='foodtags', on_delete=models.CASCADE, default='')

#   def __str__(self):
#     return f'{self.tag}'
