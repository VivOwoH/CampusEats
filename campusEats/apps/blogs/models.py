from django.db import models
from apps.user.models import CustomUser
from apps.restaurants.models import Restaurant

class Blog(models.Model):
    author = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey("user.CustomUser", on_delete=models.CASCADE)
    article = models.ForeignKey('Blog', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.article.title}"

