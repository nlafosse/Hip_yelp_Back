from .models import Food, Drink
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import FoodSerializer, DrinkSerializer

# FoodViewSet
class FoodViewSet(viewsets.ModelViewSet):
  queryset = Food.objects.all()
  serializer_class = FoodSerializer
  permission_classes = [permissions.AllowAny]

# DrinkViewSet
class DrinkViewSet(viewsets.ModelViewSet):
  queryset = Drink.objects.all()
  serializer_class = DrinkSerializer
  permission_classes = [permissions.AllowAny]
