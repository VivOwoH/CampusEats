from django.db import models
from enum import Enum

from restaurants.models import Restaurant

class UserType(Enum):
    USER = 'user'
    ADMIN = 'admin'

class User(models.Model):
    UserID = models.AutoField(primary_key = True)
    UserName = models.CharField(max_length=255, null = False)
    Password = models.CharField(max_length=255, null = False)
    Email = models.CharField(max_length=255)
    Phone = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')],
    )
    Role = models.CharField(
        max_length=5,
        choices=[(tag.name, tag.value) for tag in UserType]
    )
    Bookmark = models.ForeignKey(Bookmark, on_delete=models.CASCADE)

class Bookmark(models.Model):
    BookmarkID = models.AutoField(primary_key = True)
    RestaurantID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class FavRestaurants(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    RestaurantID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['UserID', 'RestaurantID'], name='unique_favourite_key')
        ]
