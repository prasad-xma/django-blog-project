from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Blog
from .forms import BlogForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

# get blogs
def blog_list(request):
    blogs = Blog.objects.filter(status='public')
    return render(request, 'blogs/blog_list.html', {'blogs': blogs})


# blog detail
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if blog.status == 'private' and blog.owner != request.user:
        return HttpResponseForbidden("This blog is private.")
    return render(request, 'blogs/blog_detail.html', {'blog': blog})

# create blog
@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = request.user
            blog.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm()
    return render(request, 'blogs/blog_form.html', {'form': form})

# edit blog
@login_required
def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if blog.owner != request.user:
        return HttpResponseForbidden("You are not allowerd to edit this blog.")
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blogs/blog_form.html', {'form': form})

# delete blog
@login_required
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    
    if blog.owner != request.user:
        return HttpResponseForbidden("You are not allowed to delete this blog...")
    blog.delete()
    
    return redirect('blog_list')