from django.db import models
from django.conf import settings

# Create your models here.

class Page(models.Model):
    
    author = models.CharField(max_length=100)
    
    recipe_title = models.CharField(max_length=100)
    
    ingredients = models.TextField()
    
    instructions = models.TextField(help_text="Write the instructions of your recipe")
    
    description = models.TextField(help_text="Write the desciption of your recipe")
    
    created = models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        return self.recipe_title
    
class Ingredient(models.Model):
    
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    
    
    
    
    