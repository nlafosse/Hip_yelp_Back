from .models import Food, Drink
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# FoodSerializer
class FoodSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Food
    fields = ['id', 'name', 'address', 'description']


# DrinkSerializer
class DrinkSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Drink
    fields = ['id', 'name', 'address', 'description']

