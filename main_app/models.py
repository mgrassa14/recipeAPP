from django.db import models
from django.urls import reverse

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    culture = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    # neededd to put get_absolute_url within the Recipe model or else update will not work
    def get_absolute_url(self):
        return reverse('detail', kwargs={'recipe_id': self.id})

    def __str__(self):
        return self.title

class Ingredients(models.Model):
    name = models.CharField(max_length=100, default='ingredient')
    quantity = models.IntegerField(default=0)
    measurment = models.CharField(max_length=100, default='measurment')
    
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}"
 