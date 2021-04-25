from .models import Food, Drink, FoodTag, DrinkTag
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# FoodSerializer
class FoodSerializer(serializers.HyperlinkedModelSerializer):
  foodTags = serializers.SlugRelatedField(many=True, slug_field='tagname', queryset=FoodTag.objects.all())
  class Meta:
    model = Food
    fields = ['id', 'name', 'group', 'address', 'description', 'photo_url', 'lon', 'lat', 'foodTags']

# FoodTagSerializer
class FoodTagsSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = FoodTag
    fields = ('tagname')

# DrinkSerializer
class DrinkSerializer(serializers.HyperlinkedModelSerializer):
  drinkTags = serializers.SlugRelatedField(many=True, slug_field='tagname', queryset=DrinkTag.objects.all())
  class Meta:
    model = Drink
    fields = ['id', 'name', 'group', 'address', 'description', 'photo_url', 'lon', 'lat', 'drinkTags']

# DrinkTagsSerializer
class DrinkTagsSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = DrinkTag
    fields = ('tagname')

