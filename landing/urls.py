from django.urls import path
from landing.views import LandingView
from accounts.views import SignupView

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('signup/', SignupView.as_view(), name='signup'),
    
]