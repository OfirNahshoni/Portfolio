from django.shortcuts import render
from . import views

# Create your views here.

def home(request):
    return render(request, 'index.html')

def posts(request):
    return render(request, 'posts.html')

def post(request):
    return render(request, 'post.html')

def profile(request):
    return render(request, 'profile.html')
