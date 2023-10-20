# user/urls.py
from django.urls import path, include, re_path as url
from . import views

urlpatterns = [
    # Other URL patterns for user-related views
    # path('login/', views.user_login, name='login'),
    # path('', views.render_base_template, name='render_base'),
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='login'),
    path('success/', views.render_success, name='success'),
    path('register/admin/', views.render_admin_dashboard, name='admin_dashboard'),
    path('register/admin/add-restaurants/', views.render_admin_add_restaurants, name='add_restaurants'),
    path('userlist/', views.user_list, name='user list'),
    path('access-denied/', views.access_denied, name='access_denied'),
    path('register/admin/update-users/', views.render_admin_updateusers, name='update_users'),
    path('update-user/', views.update_user, name='update_user'),
    path('edit/<id>', views.edit_user, name='editData'),
    path('delete/<id>', views.delete_user, name='deleteData'),
    path('insert_restaurant/', views.insert_restaurant, name='insertRestaurants'),
    path('register/admin/update-restaurants/', views.edit_restaurant, name='editRestaurant'),
    path('edit_rest/<id>', views.edit_restaurant_details, name='editRestaurantDetails'),
    path('delete_rest/<id>', views.delete_restaurant, name='deleteRestaurant'),
    


]
