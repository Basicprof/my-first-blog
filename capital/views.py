from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from .models import Cocos
# Create your views here.
def post_list(request):
    posts = Cocos.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'capital/post_list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Cocos, slug=post, status='published',publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'capital/post_detail.html', {'post': post})
