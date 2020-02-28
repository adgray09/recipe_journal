from django.contrib import admin
from recipes.models import Page

class PageAdmin(admin.ModelAdmin):
    model = Page

admin.site.register(Page, PageAdmin)