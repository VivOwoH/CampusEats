# user/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'You have been successfully logged in.')
                return redirect('dashboard')  # Redirect to the dashboard or any other desired page
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'user/base.html', {'form': form})



def render_base_template(request):
    return render(request, 'base.html')

def user_register(request):
    if request.method == 'POST':
        return redirect('render_base_template')  
    
    return render(request, 'user/register.html')

def render_success(request):
    return render(request, 'user/success.html')