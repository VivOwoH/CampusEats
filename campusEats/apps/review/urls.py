from django.urls import path
from . import views

urlpatterns = [
    path('create-review/', views.create_review, name='create_review'),
    path('edit-review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete-review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('display-review/<int:review_id>/', views.display_reviews, name='display_reviews'),
]
