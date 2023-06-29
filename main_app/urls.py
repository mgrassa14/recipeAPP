from django.urls import path
# import all the functions from the views.py file and attach them to the variable named views
from . import views

urlpatterns = [
    # localhost:8000
    path('', views.home, name='home'),
    # localhost:8000/about
    path('about/', views.about, name='about'),
]