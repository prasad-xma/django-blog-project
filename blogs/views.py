from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Blog
from .forms import BlogForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

