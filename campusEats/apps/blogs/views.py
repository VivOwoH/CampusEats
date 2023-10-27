from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *

from .models import Blog, Comment
from .forms import BlogForm, CommentForm

global gloabl_user

gloabl_user = None

def blog_test(request):
    context = {'user': gloabl_user}
    return render(request, 'blogs/test.html', context)

# List all blog posts
def blog_list(request):
    blogs = Blog.objects.all()
    global gloabl_user
    gloabl_user = CustomUser.get_global_user()
    print(gloabl_user)
    context = {'blogs': blogs, 'user': gloabl_user}
    return render(request, 'blogs/list_blogs.html', context)

# View details of a single blog post
def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comments = Comment.objects.filter(article=blog)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = blog
            comment.user = request.user  # Assuming user is logged in
            comment.save()
            return redirect('blog_detail', blog_id=blog.id)  # Redirect to the same blog detail page

    else:
        form = CommentForm()

    context = {'blog': blog, 'comments': comments, 'form': form, 'user': gloabl_user}
    return render(request, 'blogs/blog_detail.html', context)

# Create a new blog post
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_blogs')
    else:
        form = BlogForm()
    context = {'form': form, 'user': gloabl_user}
    return render(request, 'blogs/blog_form.html', context)

# Update an existing blog post
def blog_update(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', blog_id=blog.id)
    else:
        form = BlogForm(instance=blog)
    context = {'form': form, 'user': gloabl_user}
    return render(request, 'blog_form.html', context)

# Delete a blog post
def blog_delete(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('blog_list')

# List comments for a specific blog post and add a new comment
def blog_comments(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comments = Comment.objects.filter(article=blog)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = blog
            comment.save()
            return redirect('blog_comments', blog_id=blog.id)
    else:
        form = CommentForm()
    context = {'blog': blog, 'comments': comments, 'form': form, 'user': gloabl_user}
    return render(request, 'blog_comments.html', context)
