from django.shortcuts import render
from . import views
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()    
    context = {'posts': posts}
    return render(request, 'index.html', context=context)

def posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts.html', context=context)

def post(request):
    return render(request, 'post.html')

def profile(request):
    return render(request, 'profile.html')
