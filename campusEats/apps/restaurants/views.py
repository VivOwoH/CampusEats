from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

def render_home(request):
    return render(request, 'restaurants/home.html')
# Create your views here.
