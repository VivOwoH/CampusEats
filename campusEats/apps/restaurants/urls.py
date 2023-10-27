# user/urls.py
from django.urls import path, include, re_path as url
from . import views
from .views import MainView, RestaurantJsonListview

urlpatterns = [
    path('', views.render_home, name='Home'),
    path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('search/all', views.restaurant_list_view, name='restaurant_list'),
    path('save_reaction/', views.save_reaction, name='save_reaction'),
    path('save_reaction/<int:review_id>/<int:reaction_id>/', views.save_reaction, name='save_reaction'),
    path('get_reaction_emoji', views.get_reaction_emoji, name='get_reaction_emoji'),

    path('', MainView.as_view(), name='main-view'),
    path('restaurants-json/<int:restaurant_id>/', RestaurantJsonListview.as_view(), name='restaurants-json-view'),
]
