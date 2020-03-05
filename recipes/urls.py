from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import forms


urlpatterns = [
    path('recipes/', views.recipe_page, name="recipe-page"),
    path('add_recipe/', views.PageCreateView.as_view(), name="new_recipe_page"),
] 


