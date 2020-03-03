from django.urls import path, include
from landing.views import LandingView
from accounts.views import SignupView
from recipes.views import PageListView

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('/recipes', PageListView.as_view(), name="recipe_page"),
]