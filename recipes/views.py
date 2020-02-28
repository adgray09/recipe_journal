from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Page
# Create your views here.

class PageListView(ListView):
    model = Page
    
    def get(self, request):
        pages = self.get_queryset().all()
        return render(request, 'page_list.html', {"pages": pages})
    
    
    
    

