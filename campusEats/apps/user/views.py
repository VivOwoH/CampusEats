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
from django.contrib import messages



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
        CustomUser.set_global_user(global_user)
        print(CustomUser.get_global_user())

        if user and (user.password == password or check_password(password, user.password)):
            # global_user = user
            if is_admin(request):
                return redirect('/register/admin')
                # return redirect(reverse('/register/admin'))  
                # return render(request, 'user/adminhome.html', {'error_message': error_message})
            # User authentication successful, log the user in (you may want to set a session variable)
            return redirect('/profile/user/account')  # Redirect to a success page after login
        else:
            # Authentication failed, handle it (e.g., display an error message)
            error_message = 'Invalid login credentials'
            return render(request, 'user/login.html', {'error_message': error_message})
    if request.method == 'GET':
        return render(request, 'user/login.html')

def user_logout(request):
    CustomUser.set_global_user(None)
    message = "Log out successful"
    messages.success(request, message, extra_tags="autoclose")  # Add a success message with an "autoclose" tag

    return redirect('/')


def access_denied(request):
    # print(message)
    # context = {'message': message}
    return render(request, 'user/access_denied.html', {'message': 'admin'})

# Custom test functions
def is_admin(request):
    # print(1, global_user.user_type)
    # user = request.user  # Retrieve the User object from the request
    # custom_user = CustomUser(user)
    if not global_user:
        return False
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
    print(type(global_user))
    # If the user is an admin, render the admin dashboard
    return render(request, 'user/adminhome.html', {'user': global_user})

@user_passes_test(is_admin, login_url='access_denied')
def update_admin(request):
    if request.method == 'POST':
        # Retrieve form data from the POST request
        username = request.POST.get('first_name')
        display_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')

        # Process the form data (you can save it to the database or perform other actions)
        # For this example, we'll just print the data to the console
        print('First Name:', username)
        print('Last Name:', display_name == '')
        print('Email:', email)
        print('Contact Number:', contact_no)
        
        user = CustomUser.get_global_user()
        try:
            if username:
                user.username = username
            if display_name:
                user.display_name = display_name
            if email:
                user.email = email
            if contact_no:
                user.contact_number = contact_no

            user.save()  # Save the changes to the user profile

            message = "Profile updated successfully"
            
        except Exception as e:
            # Handle the IntegrityError (e.g., unique constraint violation)
            message = "An error occurred while updating the profile."
        messages = list()
        messages.append(message)

        return render(request, 'user/adminhome.html', {'messages': messages, 'user':user})


        # You can also return a response to the user, e.g., a success message
        # return HttpResponse('Profile updated successfully.')

    # If it's not a POST request, render the HTML form
    # return render(request, 'user/adminhome.html')



#render the admin update users html
def render_admin_updateusers(request):
    # print("hello")
    data = CustomUser.objects.all()
    # print(data)
    context = {"data":data}
    # print(context)
    return render(request,'user/admin-update-users.html', context)



def update_user(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        role = request.POST.get('role')
        print(name, email, role)
        query=CustomUser(username=name, email=email,user_type=role)
        query.save()
        return redirect('/register/admin/update-users/')
    return render(request, 'user/admin-update-users.html', {'user': global_user})


def edit_user(request, id):

    #save the updated information
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        role = request.POST.get('role')

        updated_d = CustomUser.objects.get(id=id)
        updated_d.username = name
        updated_d.email = email
        updated_d.user_type= role
        updated_d.save()
        return redirect('/register/admin/update-users/')
    
    d = CustomUser.objects.get(id=id)
    context={"d":d}
    return render(request,"user/edit.html", context)

def delete_user(request, id):
    d = CustomUser.objects.get(id=id)
    d.delete()
    return redirect("/register/admin/update-users/")

def render_user_dashboard(request):
    return render(request, 'user/userhome.html', {'user': global_user})

# please help implement the tops and bookmarks
def render_user_tops(request):
    tops = {}
    return render(request, 'user/user-tops.html', {'user': global_user, 'tops': tops})

def render_user_bookmarks(request):
    bookmarks = {}
    return render(request, 'user/user-bookmarks.html', {'user': global_user, 'bookmarks': bookmarks})

def render_user_email(request):
    return render(request, 'user/user-email.html', {'user': global_user})
  


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
                return redirect('login')  # Registration successful, redirect to success page
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

def is_blogger(global_user):
    return global_user.user_type == UserType.BLOGGER.value

def user_list(request):
    # Query all users from the CustomUser model
    users = CustomUser.objects.all()

    # Pass the list of users to the template
    return render(request, 'user/success.html', {'users': users})

def render_success(request):
    if request.method == "POST":
        id=request.POST.get('restaurant_id')
        print(id)
        name=request.POST.get('name')
        description=request.POST.get('restaurant_desc')
        location=request.POST.get('location')
        img_url=request.POST.get('img_url')
        phone = request.POST.get('phone')
        price = request.POST.get('price')
        dine_in = request.POST.get('dine_in')
        delivery = request.POST.get('delivery')
        reservable = request.POST.get('reservable')
        serves_wine = request.POST.get('serves_wine')
        
        #get updated restaurant data
        updated_r = Restaurant.objects.get(RestaurantID=id) 
        print(updated_r)  
        try:
            updated_r.Name = name
            updated_r.Location = location
            updated_r.Description = description
            updated_r.ImageURL = img_url
            
            # save the updated data into the db
            updated_r.save()
            print(updated_r.Name)
        except Exception as e:
            print(e) 

        return redirect('/register/admin/update-resturants/')

    rest_id = Restaurant.objects.get(RestaurantID=id)
    print(rest_id)
    context_ = {"rest_id":rest_id}
    # return render(request, "user/edit-restaurant.html",context_)
    return render(request, 'user/success.html', {'user': global_user})


# for the rendering of the admin add resturants page
#@user_passes_test(is_admin, login_url='access_denied')

def render_admin_add_restaurants(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        role = request.POST.get('role')

        updated_d = CustomUser.objects.get(id=id)
        updated_d.username = name
        updated_d.email = email
        updated_d.user_type= role
        updated_d.save()
        return redirect('/register/admin/update-users/')
    return render(request,'user/admin-add-restaurants.html')

def insert_restaurant(request):
    if request.method == "POST":
        name=request.POST.get('name')
        description=request.POST.get('restaurant_desc')
        location=request.POST.get('location')
        img_url=request.POST.get('img_url')
        phone = request.POST.get('phone')
        price = request.POST.get('price')
        dine_in = request.POST.get('dine_in')
        delivery = request.POST.get('delivery')
        reservable = request.POST.get('reservable')
        serves_wine = request.POST.get('serves_wine')
        query = Restaurant(Name=name, Location=location,Description=description)
        query.save()
        print(name, location)
    return render(request,'user/admin-add-restaurants.html')

# edit restuarant details
def edit_restaurant(request):
    rest_data = Restaurant.objects.all()
    context_={"rest_data":rest_data}
    return render(request,'user/admin-update-restaurants.html', context_)


# called when the edit restaurant button is clicked the form is calls the submit function
def edit_restaurant_details(request, id):
    print(id)
    if request.method == "POST":
        name=request.POST.get('restaurant_id')
        name=request.POST.get('name')
        description=request.POST.get('restaurant_desc')
        location=request.POST.get('location')
        img_url=request.POST.get('img_url')
        phone = request.POST.get('phone')
        price = request.POST.get('price')
        dine_in = request.POST.get('dine_in')
        delivery = request.POST.get('delivery')
        reservable = request.POST.get('reservable')
        serves_wine = request.POST.get('serves_wine')
        
        #get updated restaurant data
        updated_r = Restaurant.objects.get(RestaurantID=id) 
        print(updated_r)  
        try:
            updated_r.Name = name
            updated_r.Location = location
            updated_r.Description = description
            updated_r.ImageURL = img_url
            
            # save the updated data into the db
            updated_r.save()
            print(updated_r.Name)
        except Exception as e:
            print(e) 

        return redirect('/register/admin/update-resturants/')

    rest_id = Restaurant.objects.get(RestaurantID=id)
    print(rest_id)
    context_ = {"rest_id":rest_id}
    return render(request, "user/edit-restaurant.html",context_)

def update_details(request, id):
    print(id)
    if request.method == "POST":
        name=request.POST.get('restaurant_id')
        name=request.POST.get('name')
        description=request.POST.get('restaurant_desc')
        location=request.POST.get('location')
        img_url=request.POST.get('img_url')
        phone = request.POST.get('phone')
        price = request.POST.get('price')
        dine_in = request.POST.get('dine_in')
        delivery = request.POST.get('delivery')
        reservable = request.POST.get('reservable')
        serves_wine = request.POST.get('serves_wine')
        
        #get updated restaurant data
        updated_r = Restaurant.objects.get(RestaurantID=id) 
        print(updated_r)  
        try:
            updated_r.Name = name
            updated_r.Location = location
            updated_r.Description = description
            updated_r.ImageURL = img_url
            
            # save the updated data into the db
            updated_r.save()
            print(updated_r.Name)
        except Exception as e:
            print(e) 

        return redirect('/register/admin/update-resturants/')

    rest_id = Restaurant.objects.get(RestaurantID=id)
    print(rest_id)
    context_ = {"rest_id":rest_id}
    return render(request, "user/edit-restaurant.html",context_)



def delete_restaurant(request, id):
    rest_id = CustomUser.object.get(id=id)
    rest_id.delete()
    return redirect('/register/admin/update-restaurants.html')


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
