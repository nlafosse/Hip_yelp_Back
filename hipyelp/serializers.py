from .models import *
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# FoodSerializer
class FoodSerializer(serializers.ModelSerializer):
  # foodTags = FoodTagsSerializer(many=True)
  class Meta:
    model = Food
    fields = '__all__'

# DrinkSerializer
class DrinkSerializer(serializers.ModelSerializer):
  # drinkTags = DrinkTagsSerializer(many=True)
  class Meta:
    model = Drink
    fields = '__all__'
