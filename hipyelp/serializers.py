from .models import Food, FoodTag
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# class FtagSerializer(serializers.HyperlinkedModelSerializer):

#   class Meta:
#     model = Ftag
#     fields = '__all__'
# FoodTagSerializer
class FoodTagSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = FoodTag
    fields = '__all__'

# FoodSerializer
class FoodSerializer(serializers.HyperlinkedModelSerializer):
  # tags = FoodTagSerializer(many=True, default='dive')
  tags = serializers.SlugRelatedField(many=True, slug_field='tagname', queryset=FoodTag.objects.all())
  class Meta:
    model = Food
    fields = '__all__'


# class PopulatedFoodTagSerializer(FoodSerializer):
#   food = FoodSerializer()
#   tags = FtagSerializer(many=True)

# class DtagSerializer(serializers.HyperlinkedModelSerializer):

#   class Meta:
#     model = Dtag
#     fields = '__all__'

# # DrinkSerializer
# class DrinkSerializer(serializers.HyperlinkedModelSerializer):
#   # drinkTags = serializers.SlugRelatedField(many=True, slug_field='tagName', queryset=DrinkTag.objects.all())
#   class Meta:
#     model = Drink
#     fields = '__all__'

# # DrinkTagsSerializer
# class DrinkTagsSerializer(serializers.HyperlinkedModelSerializer):
#   class Meta:
#     model = DrinkTag
#     fields = '__all__'

# class PopulatedDrinkTagSerializer(DrinkSerializer):
#   drink = DrinkSerializer()
#   tags = DtagSerializer(many=True)
