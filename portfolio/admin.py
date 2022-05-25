from django.contrib import admin
from .models import Portfolio

@admin.register(Portfolio)
class PortforioAdmin(admin.ModelAdmin):
    list_display = ['title','image','description']
