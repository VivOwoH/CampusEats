# user/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .models import *  # Import your models here

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

# def user_register(request):
#     if request.method == 'POST':
#         # Assuming you're using Django's built-in User model
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         print(username)
#         # Check if passwords match
#         if password1 == password2:
#             # Create a new User instance
#             user = User.objects.register_user(username=username, email=email, password=password1)
#             # Save the user instance to the database
#             user.save()
#             # Log the user in
#             # login(request, user)
#             return redirect('success')  
    
#     return render(request, 'user/register.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.register_user(username, email, password1, password2):
            return redirect('success')  # Registration successful, redirect to success page
        else:
            # Registration failed, handle it (e.g., display an error message)
            return render(request, 'user/register.html', {'error_message': 'Registration failed'})

    return render(request, 'user/register.html')

def render_success(request):
    return render(request, 'user/success.html')

# for the rendering of the admin
def render_admin_dashboard(request):
    return render(request,'user/adminhome.html')