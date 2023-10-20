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
    path('profile/user/account', views.render_user_dashboard, name='user_dashboard'),
    path('profile/user/email', views.render_user_email, name='user_email'),
    path('profile/user/tops', views.render_user_tops, name='user_top_restaurants'),
    path('profile/user/bookmarks', views.render_user_bookmarks, name='user_bookmarks'),
]
