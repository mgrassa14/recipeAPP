from django.shortcuts import render
from .models import Recipe

# Create your views here.
from django.http import HttpResponse

# ===========================================================
# class Recipe:
#   def __init__(self, title, culture, description, image):
#     self.title = title
#     self.culture = culture
#     self.description = description
#     self.image = image

# recipes = [
#   Recipe('Pasta Bolgonese', 'Italian', 'spegetti pasta with a ground beef tomato sauce', 'https://www.fromvalerieskitchen.com/wordpress/wp-content/uploads/2022/09/Pasta-Bolognese-SQ-175.jpg'),
#   Recipe('PB&J', 'American', 'penut butter and jelly sandwich with white bread', 'https://www.seriouseats.com/thmb/GF4MI4q0ARhLNZ8BC7Q8lL16w-E=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/__opt__aboutcom__coeus__resources__content_migration__serious_eats__seriouseats.com__images__20070401istockpbjbeauty-ab4898b093c14b65b7606ec1152acbe0.jpg'),
#   Recipe('Pesto Pasta', 'Italian', 'spegetti pasta with a pesto sauce. Includes cheese', 'https://richanddelish.com/wp-content/uploads/2023/02/creamy-pesto-pasta-1.jpg'),
#   Recipe('Pasta Bolgonese', 'Italian', 'spegetti pasta with a ground beef tomato sauce', '')
# ]
# ============================================================

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def recipes_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', { 'recipes': recipes })

def recipes_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes/detail.html', { 'recipe': recipe })