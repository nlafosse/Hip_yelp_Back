from .models import Food, Drink, FoodTag, DrinkTag
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# FoodTagSerializer
class FoodTagsSerializer(serializers.ModelSerializer):
  class Meta:
    model = FoodTag
    fields = ['tags']

# FoodSerializer
class FoodSerializer(serializers.ModelSerializer):
  foodTags = FoodTagsSerializer(many=True)
  class Meta:
    model = Food
    fields = '__all__'


# DrinkTagsSerializer
class DrinkTagsSerializer(serializers.ModelSerializer):
  class Meta:
    model = DrinkTag
    fields = ['tags']

# DrinkSerializer
class DrinkSerializer(serializers.ModelSerializer):
  drinkTags = DrinkTagsSerializer(many=True)
  class Meta:
    model = Drink
    fields = '__all__'


