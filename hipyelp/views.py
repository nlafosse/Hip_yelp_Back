from .models import Food, Drink
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *

# FoodViewSet
class FoodViewSet(viewsets.ModelViewSet):
  queryset = Food.objects.filter()
  serializer_class = FoodSerializer
  permission_classes = [permissions.AllowAny]

# DrinkViewSet
class DrinkViewSet(viewsets.ModelViewSet):
  queryset = Drink.objects.filter()
  serializer_class = DrinkSerializer
  permission_classes = [permissions.AllowAny]

# FoodTagViewSet
class FoodTagsViewSet(viewsets.ModelViewSet):
  queryset = FoodTag.objects.all()
  serializer_class = FoodTagsSerializer
  permission_classes = [permissions.AllowAny]

# DrinkTagViewSet
class DrinkTagsViewSet(viewsets.ModelViewSet):
  queryset = DrinkTag.objects.all()
  serializer_class = DrinkTagsSerializer
  permission_classes = [permissions.AllowAny]
