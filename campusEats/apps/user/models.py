from django.db import models
from django.core.validators import RegexValidator  # Import RegexValidator here
from enum import Enum
from django.contrib.auth.hashers import make_password
from apps.restaurants.models import Restaurant

# Defining an enumeration for user types.
class UserType(Enum):
    USER = 'user'
    ADMIN = 'admin'
    BLOGGER = 'blogger'

# Global user variable initialized as None.
global global_user
global_user = None

# CustomUser model for user management.
class CustomUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    user_type = models.CharField(
        max_length=10,
        choices=[(user_type.value, user_type.name) for user_type in UserType],
        default=UserType.USER.value
    )
    contact_number = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.username

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @classmethod
    def set_global_user(cls, user):
        global global_user
        global_user = user

    @classmethod
    def get_global_user(cls):
        return global_user

    @classmethod
    def register_user(cls, username, email, password1, password2):
        # Check if passwords match
        if password1 != password2:
            return False  # Passwords do not match, registration failed

        # Hash the password using Django's make_password
        hashed_password = make_password(password1)

        # Create a new CustomUser instance with the hashed password
        user = cls(username=username, email=email, password=hashed_password, display_name=username)
        user.save()
        return True

# Bookmark model for storing user bookmarks.
class Bookmark(models.Model):
    BookmarkID = models.AutoField(primary_key=True)
    RestaurantID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
