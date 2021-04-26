from .models import *
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

  def create(self, validated_data):
    foodTags_data = validated_data.pop('foodTags')
    food = Food.objects.create(**validated_data)
    for foodTags_data in foodTags_data:
      FoodTag.objects.create(foodtags=foodtags, **foodTags_data)
      FoodTag.objects.create(food=food, **foodTags_data)
    return food


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

  def create(self, validated_data):
    drinkTags_data = validated_data.pop('drinkTags')
    drink = Drink.objects.create(**validated_data)
    for drinkTags_data in drinkTags_data:
      DrinkTag.objects.create(drinktags=drinktags, **drinkTags_data)
      DrinkTag.objects.create(drink=drink, **drinkTags_data)
    return drink

