from .models import Food, Drink, HotSpotTag
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# FoodSerializer
class FoodSerializer(serializers.HyperlinkedModelSerializer):
  tags = serializers.SlugRelatedField(many=True, slug_field='tagname', queryset=HotSpotTag.objects.all())
  class Meta:
    model = Food
    fields = ['id', 'name', 'group', 'address', 'description', 'photo_url', 'lon', 'lat', 'tags']

# HotSpotTagSerializer
class TagsSerializer(serializers.HyperlinkedModelSerializer):
  class Metal:
    model = HotSpotTag
    fields = ('tagname')


# DrinkSerializer
class DrinkSerializer(serializers.HyperlinkedModelSerializer):
  tags = serializers.SlugRelatedField(many=True, slug_field='tagname', queryset=HotSpotTag.objects.all())
  class Meta:
    model = Drink
    fields = ['id', 'name', 'group', 'address', 'description', 'photo_url', 'lon', 'lat', 'tags']

