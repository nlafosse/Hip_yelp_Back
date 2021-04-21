from .models import HotSpot, Food, Drink
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# HotSpotSerializer
class HotSpotSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = HotSpot
    fields = ['id', 'category']

# FoodSerializer
class FoodSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Food
    fields = ['id', 'name', 'address', 'comment']


# DrinkSerializer
class DrinkSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Drink
    fields = ['id', 'name', 'address', 'comment']

