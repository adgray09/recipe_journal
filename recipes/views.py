from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Page
from django.http import HttpResponse
from django.template import loader

# Create your views here.

class PageListView(ListView):
    model = Page
    
    def get(self, request):
        pages = self.get_queryset().all()
        return render(request, 'recipes/page_list.html', {"pages": pages})
    
def recipe_page(request):
    recipes_list = Page.objects.all()
    context = {"recipes_list": recipes_list,}
    template = loader.get_template('recipes/index.html')
    return HttpResponse(template.render(context, request))
        
    
    
    

