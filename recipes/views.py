from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Page
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.edit import CreateView
from .forms import PageForm
from django.urls import reverse_lazy


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

class PageCreateView(CreateView):
    def get(self, request):
        context = {"form": PageForm()}
        return render(request, 'recipes/recipe_form.html', context)
    
    def post(self, request):
        form = PageForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return HttpResponseRedirect(reverse_lazy('landing'))
        return render(request, 'landing.html', {'form': form})
            

        
    
    
    

