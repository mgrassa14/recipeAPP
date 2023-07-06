from django.contrib import admin
# import your models here
from .models import Recipe, Ingredients

# Register your models here.
admin.site.register(Recipe)

admin.site.register(Ingredients)