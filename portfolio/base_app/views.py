from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . import views
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.filter(is_active=True, featured=True)[0:3]

    context = {'posts': posts}
    return render(request, 'index.html', context=context)

def posts(request):
    posts = Post.objects.filter(is_active=True)

    context = {'posts': posts}
    return render(request, 'posts.html', context=context)

def post(request, pk):
    post = Post.objects.get(id=pk)

    context = {'post': post}
    return render(request, 'post.html', context=context)

def profile(request):
    return render(request, 'profile.html')

# CRUD Views

@login_required(login_url="home")
def createPost(request):
    form = PostForm()

    # Handle POST request
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # Check
        if form.is_valid():
            form.save()
        return redirect('posts')
    context = {'form': form}
    return render(request, 'post_form.html', context=context)