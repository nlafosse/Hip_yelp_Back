from .models import Food
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import FoodSerializer

# FoodViewSet
class FoodViewSet(viewsets.ModelViewSet):
  queryset = Food.objects.filter()
  serializer_class = FoodSerializer
  permission_classes = [permissions.AllowAny]

# # DrinkViewSet
# class DrinkViewSet(viewsets.ModelViewSet):
#   queryset = Drink.objects.filter()
#   serializer_class = DrinkSerializer
#   permission_classes = [permissions.AllowAny]
