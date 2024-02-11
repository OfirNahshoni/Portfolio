from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from . import views

from .models import Post, Tag
from .forms import PostForm
from .filters import PostFilter

def home(request):
    posts = Post.objects.filter(is_active=True, featured=True)[0:3]
    tags = Tag.objects.all()

    context = {'posts': posts, 'tags': tags}
    return render(request, 'index.html', context=context)

def posts(request):
    posts = Post.objects.filter(is_active=True)
    posts_filter = PostFilter(request.GET, queryset=posts)
    posts = posts_filter.qs  # To apply the search from the 'posts_filter'

    # Pagination
    page = request.GET.get('page')
    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'posts': posts, 'posts_filter': posts_filter}
    return render(request, 'posts.html', context=context)

def post(request, slug):
    post = Post.objects.get(slug=slug)

    context = {'post': post}
    return render(request, 'post.html', context=context)

# CRUD Views - Create , Update , Delete

@login_required(login_url="home")
def createPost(request):
    form = PostForm()

    # Handle POST request
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # Check validation
        if form.is_valid():
            form.save()
            
        return redirect('posts')

    context = {'form': form}
    return render(request, 'post_form.html', context=context)

@login_required(login_url="home")
def updatePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)

    # Handle POST request
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        # Check
        if form.is_valid():
            form.save()
        return redirect('posts')

    context = {'form': form}
    return render(request, 'post_form.html', context=context)

@login_required(login_url="home")
def deletePost(request, slug):
    post = Post.objects.get(slug=slug)

    # Handle POST request
    if request.method == 'POST':
        post.delete()
        return redirect('posts')

    context = {'post': post}
    return render(request, 'delete_post.html', context=context)


# Sending Email (from Contact Form in home page)
def sendEmail(request):
    if request.method == 'POST':
        template = render_to_string('email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })
        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['ofirnahnn221@gmail.com']
        )

        email.fail_silently = False
        email.send()

    return render(request, 'email_sent.html')