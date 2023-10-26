# user/urls.py
from django.urls import path, include, re_path as url
from . import views
from .views import MainView, RestaurantJsonListview

urlpatterns = [
    # Other URL patterns for user-related views
    # path('login/', views.user_login, name='login'),
    path('', views.render_home, name='Home'),
    path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('search/all', views.restaurant_list_view, name='restaurant_list'),
    path('', MainView.as_view(), name='main-view'),
    path('restaurants-json/<int:restaurant_id>/', RestaurantJsonListview.as_view(), name='restaurants-json-view'),
]
