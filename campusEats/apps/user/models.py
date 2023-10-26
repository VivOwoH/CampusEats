from django.db import models
from django.core.validators import RegexValidator  # Import RegexValidator here
from enum import Enum
from django.contrib.auth.hashers import make_password
from apps.restaurants.models import Restaurant

class UserType(Enum):
    USER = 'user'
    ADMIN = 'admin'
    BLOGGER = 'blogger'

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(username, email, password, **extra_fields)
    
#     def create_user(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(username, email, password, **extra_fields)

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=255, unique=True, default='user')
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)
#     display_name = models.CharField(max_length=255, blank=True, null=True)
#     user_type = models.CharField(
#         max_length=10,
#         choices=[(user_type.value, user_type.name) for user_type in UserType],
#         default=UserType.USER.value
#     )
#     contact_number = models.PositiveIntegerField(blank=True, null=True)

#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []

#     @property
#     def is_anonymous(self):
#         return False

#     @property
#     def is_authenticated(self):
#         return True

#     def __str__(self):
#         return self.email




# ************************
class UserType(Enum):
    USER = 'user'
    ADMIN = 'admin'
    BLOGGER = 'blogger'

# Uncomment the CustomUser class definition
class CustomUser(models.Model):
    # UserID = models.AutoField(primary_key = True)
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
# **************************

# class Restaurant(models.Model):
#     RestaurantID = models.AutoField(primary_key=True)
#     Name = models.CharField(max_length=255, null=False)
#     Location = models.CharField(max_length=255, null=True)
#     Description = models.CharField(max_length=255, null=True)
#     ImageURL = models.CharField(max_length=255, null=True)


class Bookmark(models.Model):
    BookmarkID = models.AutoField(primary_key=True)
    RestaurantID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

# class FavRestaurants(models.Model):
#     UserID = models.ForeignKey(User, on_delete=models.CASCADE)
#     RestaurantID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['UserID', 'RestaurantID'], name='unique_favourite_key')
#         ]

# python manage.py makemigrations
# python manage.py migrate