# user/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .models import *  # Import your models here
from django.db import IntegrityError

from .models import CustomUser  # Import your CustomUser model

def user_login(request):
    if request.method == 'POST':
        username_or_email = request.POST['id']  # This field can accept both username and email
        password = request.POST['password']
        print(username_or_email, password )
        # Try to find a user with the provided username or email
        # try:
        #     user = CustomUser.objects.get(username=username_or_email)  # Try to match by username
        #     print(user)
        # except CustomUser.DoesNotExist:
        try:
            user = CustomUser.objects.get(email=username_or_email)  # Try to match by email
            print(user)
        except CustomUser.DoesNotExist:
            user = None  # If user doesn't exist, set to None

        if user and user.password == password:
            # User authentication successful, log the user in (you may want to set a session variable)
            return redirect('success')  # Redirect to a success page after login
        else:
            # Authentication failed, handle it (e.g., display an error message)
            error_message = 'Invalid login credentials'
            return render(request, 'user/login.html', {'error_message': error_message})

    return render(request, 'user/login.html')



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

        try:
            if CustomUser.register_user(username, email, password1, password2):
                return redirect('success')  # Registration successful, redirect to success page
            else:
                error_message = 'Registration failed'
                # Render the page and trigger the JavaScript function to show the error popup
                return render(request, 'user/register.html', {'error_message': error_message})
        except IntegrityError as e:
            # Handle the integrity constraint violation (e.g., email already exists)
            error_message = 'Email already exists'
            # Render the page and trigger the JavaScript function to show the error popup
            return render(request, 'user/register.html', {'error_message': error_message})
    return render(request, 'user/register.html')


def user_list(request):
    # Query all users from the CustomUser model
    users = CustomUser.objects.all()
    print("idk", users[4].email)
    print("idk", users[4].password)

    # Pass the list of users to the template
    return render(request, 'user/success.html', {'users': users})

def render_success(request):
    return render(request, 'user/success.html')

# for the rendering of the admin
def render_admin_dashboard(request):
    return render(request,'user/adminhome.html')

# for the rendering of the admin add resturants page
def render_admin_add_restaurants(request):
    return render(request,'user/admin-add-restaurants.html')
    # users = CustomUser.objects.all()
    # print("idk", users)
    # # Pass the list of users to the template
    # return render(request, 'user/success.html', {'users': users})