# user/urls.py
from django.urls import path, include, re_path as url
from . import views

urlpatterns = [
    # Other URL patterns for user-related views
    # path('login/', views.user_login, name='login'),
    path('', views.render_home, name='Home'),
    path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('search/all', views.restaurant_list_view, name='restaurant_list'),
    path('save_reaction/', views.save_reaction, name='save_reaction'),
    path('save_reaction/<int:review_id>/<int:reaction_id>/', views.save_reaction, name='save_reaction'),
    path('get_reaction_emoji', views.get_reaction_emoji, name='get_reaction_emoji'),

]
