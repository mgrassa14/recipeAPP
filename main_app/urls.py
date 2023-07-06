from django.urls import path
# import all the functions from the views.py file and attach them to the variable named views
from . import views

urlpatterns = [
    # localhost:8000
    path('', views.home, name='home'),
    # localhost:8000/about
    path('about/', views.about, name='about'),
    # localhost:8000/recipes
    path('recipes/', views.recipes_index, name='index'),
    # localhost:8000/recipes/1
    path('recipes/<int:recipe_id>/', views.recipes_detail, name='detail'),
    # 
    path('recipes/create', views.RecipeCreate.as_view(), name='recipes_create'),
    
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipes_update'),
    
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipes_delete'),
]