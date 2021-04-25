from .models import Food
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# class TagSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Tag
#     fields = ['tags']

# FoodSerializer
class FoodSerializer(serializers.ModelSerializer):
  # tags = FoodTagSerializer(many=True, default='dive')
  # tags = serializers.SlugRelatedField(many=True, slug_field='tagname', queryset=FoodTag.objects.all())
  tags = serializers.StringRelatedField(many=True)

  class Meta:
    model = Food
    fields = '__all__'

#   def create(self, validated_data):
#     tags_data=calidated_data.pop('tags')
#     food = Food.objects.create(**validated_data)
#     for tag_data in tags_data:
#       Tag.objects.create(food=food, **tag_data)
#     return food

# >>> data = {
#   'name': '',
#   'group': '',
#   'default': '',
#   'address': '',
#   'description': '',
#   'photo_url': '',
#   'lat': '',
#   'lon': '',
#   'tags': [
#     'tags': ''
#   ],
# }
# >>> serializer = FoodSerializer(data=data)
# >>> serializer.is_valid()
# True
# >>> serializer.save()
# <Food: Food object>