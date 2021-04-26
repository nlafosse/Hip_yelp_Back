from django.contrib import admin
from .models import Food, Drink, FoodTag, DrinkTag

# Register your models here.
admin.site.register(Food)
admin.site.register(Drink)
admin.site.register(FoodTag)
admin.site.register(DrinkTag)
