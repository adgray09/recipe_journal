from django.shortcuts import render
from django.views.generic import CreateView

# Create your views here.

class LandingView(CreateView):
    """ Class to render landingpage. """

    def get(self, request):
        """ returns landing page. """
        return render(request, 'landing/index.html')
    
    def __str__(self):
        return self.name
