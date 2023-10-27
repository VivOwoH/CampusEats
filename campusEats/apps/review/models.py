from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.restaurants.models import Restaurant
from apps.user.models import CustomUser
from django import forms



# Review models below
class Review(models.Model):
    ReviewID = models.AutoField(primary_key = True)
    RestaurantID = models.ForeignKey('restaurants.Restaurant', on_delete = models.CASCADE)
    UserID = models.ForeignKey('user.CustomUser', on_delete=models.SET_NULL, null=True)
    ParentReviewID = models.ForeignKey('self', null = True, blank = True, on_delete=models.SET_NULL)
    Rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    Description = models.CharField(max_length = 500, null = True, blank = True)
    Timestamp = models.DateTimeField(auto_now_add = True)
    # Field to store user reactions (for example, as a comma-separated list of reaction IDs)
    user_reactions = models.CharField(max_length=1000, blank=True, null=True)
    extra = models.CharField(max_length=1000, blank=True, null=True)  


class Reaction(models.Model):
    name = models.CharField(max_length=50)
    emoji = models.CharField(max_length=10)  

class ReactionForm(forms.Form):
    reaction = forms.ModelChoiceField(
        queryset=Reaction.objects.all(),
        empty_label=None,  # Disable empty label
    )
def get_restaurant_reviews(restaurantID):
    """
    Get all reviews for a specific user.
    """
    return Review.objects.filter(RestaurantID=restaurantID)

def get_restaurant_raction_for_review(review_id):
    """
    Get all reviews for a specific user.
    """
    review = Review.objects.get(ReviewID=review_id)
    emoji_ids = review.user_reactions
    if emoji_ids is None:
        return 
    emoji_ids = emoji_ids.split(",") 

    emoji_count = {}  

    reactions = [Reaction.objects.get(pk=int(i)) for i in emoji_ids]

    for reaction in reactions:
        emoji = reaction.emoji
        if emoji in emoji_count:
            emoji_count[emoji] += 1
        else:
            emoji_count[emoji] = 1

    
    return emoji_count
class React(models.Model):
    review = models.ForeignKey('Review', on_delete=models.CASCADE)
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE)
    init_reacts = models.ForeignKey('InitReacts', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['id', 'user', 'review']
class InitReacts(models.Model):
    value = models.CharField(max_length=100)


