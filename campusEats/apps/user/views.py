# user/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .models import *  # Import your models here
from django.db import IntegrityError
from django.contrib.auth.hashers import check_password
from .models import CustomUser  # Import your CustomUser model
from django.contrib.auth.decorators import user_passes_test
from .models import CustomUser

global_user = None


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
            user = CustomUser.objects.get(username=username_or_email)  # Try to match by username
        except CustomUser.DoesNotExist:
            try:
                user = CustomUser.objects.get(email=username_or_email)  # Try to match by email
            except CustomUser.DoesNotExist:
                user = None  # If user doesn't exist, set to None
        global global_user
        global_user = user
        print(global_user, type(global_user), global_user.user_type)
        if user and (user.password == password or check_password(password, user.password)):
            # User authentication successful, log the user in (you may want to set a session variable)
            return redirect('success')  # Redirect to a success page after login
        else:
            # Authentication failed, handle it (e.g., display an error message)
            error_message = 'Invalid login credentials'
            return render(request, 'user/login.html', {'error_message': error_message})

    return render(request, 'user/login.html')

def access_denied(request):
    # print(message)
    # context = {'message': message}
    return render(request, 'user/access_denied.html', {'message': 'admin'})

# Custom test functions
def is_admin(request):
    # print(1, global_user.user_type)
    # user = request.user  # Retrieve the User object from the request
    # custom_user = CustomUser(user)
    return global_user.user_type == UserType.ADMIN.value
# for the rendering of the admin
# @user_passes_test(is_admin, login_url='access_denied')
# def render_admin_dashboard(request):
#     # return render(request,'user/adminhome.html')
#     return access_denied(request, "admin")

@user_passes_test(is_admin, login_url='access_denied')
def render_admin_dashboard(request):
    if not is_admin(request.user):
        return access_denied(request,  message='admin')  # Pass the message to the access_denied view

    # If the user is an admin, render the admin dashboard
    return render(request, 'user/adminhome.html', {'user': global_user})

def admin_profile(request):
    if request.method == 'POST':
        # Retrieve form data from the POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')

        # Process the form data (you can save it to the database or perform other actions)
        # For this example, we'll just print the data to the console
        print('First Name:', first_name)
        print('Last Name:', last_name)
        print('Email:', email)
        print('Contact Number:', contact_no)

        # You can also return a response to the user, e.g., a success message
        return HttpResponse('Profile updated successfully.')

    # If it's not a POST request, render the HTML form
    return render(request, 'admin_profile.html')



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


# # Custom test functions
# def is_admin(global_user):
#     print(1, global_user.user_type)
#     return global_user.user_type == UserType.ADMIN.value

def is_blogger(global_user):
    return global_user.user_type == UserType.BLOGGER.value

def user_list(request):
    # Query all users from the CustomUser model
    users = CustomUser.objects.all()

    # Pass the list of users to the template
    return render(request, 'user/success.html', {'users': users})

def render_success(request):
    return render(request, 'user/success.html')

# def access_denied(request, message=None):
#     print(message)
#     context = {'message': message}
#     return render(request, 'user/access_denied.html', context)


# for the rendering of the admin add resturants page
@user_passes_test(is_admin, login_url='access_denied')
def render_admin_add_restaurants(request):
    return render(request,'user/admin-add-restaurants.html', "admin")
    # users = CustomUser.objects.all()
    # print("idk", users)
    # # Pass the list of users to the template
    # return render(request, 'user/success.html', {'users': users})


# Views restricted to admin and blogger roles
@user_passes_test(is_admin, login_url='access_denied')
def admin_view(request):
    # This view is only accessible to admin users
    # Your view logic here
    return render(request, 'user/usertype.html')


@user_passes_test(is_blogger, login_url='access_denied')
def blogger_view(request):
    # This view is only accessible to blogger users
    # Your view logic here
    pass
