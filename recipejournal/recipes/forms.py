from django import forms    
from recipes.models import Page

class PageForm(forms.ModelForm):
    model = Page