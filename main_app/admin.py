from django.contrib import admin
# import your models here
from .models import Recipe

# Register your models here.
admin.site.register(Recipe)