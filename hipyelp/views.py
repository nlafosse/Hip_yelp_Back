from .models import Food
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import FoodSerializer

# FoodViewSet
class FoodViewSet(viewsets.ModelViewSet):
  queryset = Food.objects.filter()
  serializer_class = FoodSerializer
  permission_classes = [permissions.AllowAny]

  # def list(self, request):
  #   pass

  # def create(self, request):
  #   pass

  # def retrieve(self, request, pk=None):
  #   pass

  # def update(self, request, pk=None):
  #   pass

  # def partial_update(self, request, pk=None):
  #   pass

  # def destroy(self, request, pk=None):
  #   pass

  # def update(self, request, *args, **kwargs):
  #   tagnames = request.data.get('fuckingtags', [])
  #   for tagname in tagnames:
  #       Food.objects.get_or_create(name=tagname)
  #   return super().update(request, *args, **kwargs)
  # def create(self, request, *args, **kwargs):
  #   tagnames = request.data.get('fuckingtags', [])
  #   for tagname in tagnames:
  #       Food.objects.get_or_create(name=tagname)
  #   return super().create(request, *args, **kwargs)

  # def update(self, request, *args, **kwargs):
  #   instance = self.get_object()
  #   tagnames = request.data.get('tags', [])
  #   serializer = self.serializer_class(instance=instance, data=request.data)
  #   if serializer.is_valid(raise_exception=True):
  #       new_object = serializer.save()
  #   if new_object:
  #       for tagname in tagnames:
  #           tag, created = FoodTag.objects.get_or_create(name=tagname)
  #           new_object.tags.add(tag)
  #   return Response(serializer.data)

# # DrinkViewSet
# class DrinkViewSet(viewsets.ModelViewSet):
#   queryset = Drink.objects.filter()
#   serializer_class = DrinkSerializer
#   permission_classes = [permissions.AllowAny]
