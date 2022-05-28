from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Portfolio

def index(request):
    return HttpResponse('Disabled account')

def portfolio_list(request):
    portfolio = Portfolio.objects.all()
    return render(request, 'portfolio/index.html',{'portfolio': portfolio})