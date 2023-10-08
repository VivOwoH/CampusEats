# user/urls.py
from django.urls import path, include, re_path as url
from . import views

urlpatterns = [
    # Other URL patterns for user-related views
    # path('login/', views.user_login, name='login'),
    # path('', views.render_base_template, name='render_base'),
    path('register/', views.user_register, name='user_register'),
    path('success/', views.render_success, name='success'),
    path('register/admin/', views.render_admin_dashboard, name='admin_dashboard'),
    path('register/admin/add-restaurants/', views.render_admin_add_restaurants, name='add_restaurants')

]
