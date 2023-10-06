from django.db import models
from django.core.validators import RegexValidator  # Import RegexValidator here
from enum import Enum

class UserType(Enum):
    USER = 'user'
    ADMIN = 'admin'

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# # from django.db import models

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, email, password=None):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password=None):
#         user = self.create_user(username, email, password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=255, unique=True)
#     email = models.EmailField(max_length=255, unique=True)
#     # Add your custom fields here
#     # ...
#     UserID = models.AutoField(primary_key=True)
#     UserName = models.CharField(max_length=255, null=False)
#     Password = models.CharField(max_length=255, null=False)
#     Email = models.CharField(max_length=255)
#     Phone = models.CharField(
#         max_length=20,
#         validators=[RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')],
#     )
#     Role = models.CharField(
#         max_length=5,
#         choices=[(tag.name, tag.value) for tag in UserType]
#     )
#     Bookmark = models.ForeignKey('Bookmark', on_delete=models.CASCADE)

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def __str__(self):
#         return self.email

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=255, null=False)
    Password = models.CharField(max_length=255, null=False)
    Email = models.CharField(max_length=255)
    Phone = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')],
    )
    Role = models.CharField(
        max_length=5,
        choices=[(tag.name, tag.value) for tag in UserType]
    )
    Bookmark = models.ForeignKey('Bookmark', on_delete=models.CASCADE)

    @classmethod
    def register_user(cls, username, email, password1, password2):
        # Check if passwords match
        if password1 != password2:
            return False  # Passwords do not match, registration failed

        # Create a new User instance
        user = cls(username=username, email=email)  # No need to specify 'Password'
        user.set_password(password1)  # Use set_password method to hash the password
        user.save()
        return True  


class Restaurant(models.Model):
    RestaurantID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, null=False)
    Location = models.CharField(max_length=255, null=True)
    Description = models.CharField(max_length=255, null=True)
    ImageURL = models.CharField(max_length=255, null=True)


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
