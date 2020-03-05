from django.forms import ModelForm
from recipes.models import Page
from django import forms

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['author', 'recipe_title', 'ingredients', 'instructions', 'description']