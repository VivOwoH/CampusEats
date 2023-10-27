from django.db import models
from apps.user.models import CustomUser
from apps.restaurants.models import Restaurant

# Defining a model for blogs
class Blog(models.Model):
    # Associating the author with a CustomUser using a foreign key
    author = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE)
    
    # Storing the title of the blog
    title = models.CharField(max_length=255)
    
    # Storing the content of the blog
    content = models.TextField()
    
    # Associating the blog with a restaurant using a foreign key (optional)
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE, blank=True, null=True)
    
    # Capturing the creation date and time of the blog
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Updating the date and time whenever the blog is modified
    updated_at = models.DateTimeField(auto_now=True)
    
    # Storing an optional image URL for the blog
    imageURL = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

# Defining a model for comments on blogs
class Comment(models.Model):
    # Associating the user with a CustomUser using a foreign key
    user = models.ForeignKey("user.CustomUser", on_delete=models.CASCADE)
    
    # Associating the comment with a blog using a foreign key
    article = models.ForeignKey('Blog', on_delete=models.CASCADE)
    
    # Storing the text content of the comment
    text = models.TextField()
    
    # Capturing the creation date and time of the comment
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Updating the date and time whenever the comment is modified
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.article.title}"
