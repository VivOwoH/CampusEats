from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.restaurants.models import Restaurant
from apps.user.models import CustomUser

# Create your models here.
# CREATE TABLE Review (
#     ReviewID INT PRIMARY KEY AUTO_INCREMENT,
#     RestaurantID INT NOT NULL,
#     UserID INT NOT NULL,
#     ParentReviewID INT, -- Reference to the parent review
#     Rating INT CHECK (Rating >= 1 AND Rating <= 5),
#     Description TEXT,
#     Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (RestaurantID) REFERENCES Restaurant (RestaurantID),
#     FOREIGN KEY (UserID) REFERENCES User (UserID),
#     FOREIGN KEY (ParentReviewID) REFERENCES Review (ReviewID) -- Self-referencing foreign key
# );

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

    def get_average_rating(self):
        """
        Calculate and return the average rating for a restaurant based on its reviews.
        """
        reviews = Review.objects.filter(RestaurantID=self.RestaurantID)
        total_ratings = sum(review.Rating for review in reviews)
        if reviews:
            return total_ratings / len(reviews)
        else:
            return 0

    def get_user_reviews(self, user):
        """
        Get all reviews for a specific user.
        """
        return Review.objects.filter(UserID=user)

    def get_parent_reviews(self):
        """
        Get all parent reviews (reviews without a ParentReviewID).
        """
        return Review.objects.filter(ParentReviewID__isnull=True)

    def get_child_reviews(self):
        """
        Get all child reviews (reviews with a ParentReviewID).
        """
        return Review.objects.filter(ParentReviewID=self)

    def has_children(self):
        """
        Check if a review has child reviews.
        """
        return Review.objects.filter(ParentReviewID=self).exists()

    def get_review_age(self):
        """
        Calculate and return the age of the review in days.
        """
        from datetime import datetime
        delta = datetime.now() - self.Timestamp
        return delta.days


# CREATE TABLE React (
# 	Id INT PRIMARY KEY AUTO_INCREMENT,
# 	reviewId INT,
# 	userId INT,
# 	InitReactsId INT,
# 	FOREIGN KEY (reviewId) REFERENCES Review(id),
# 	FOREIGN KEY (userId) REFERENCES Users(id),
# 	FOREIGN KEY (InitReactsId) REFERENCES InitReacts(Id),
# 	CONSTRAINT PK_React PRIMARY KEY (Id, userId, reviewId)
# );

class React(models.Model):
    review = models.ForeignKey('Review', on_delete=models.CASCADE)
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE)
    init_reacts = models.ForeignKey('InitReacts', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['id', 'user', 'review']

# CREATE TABLE InitReacts (
# 	Id INT PRIMARY KEY AUTO_INCREMENT,
# 	Value VARCHAR(100)
# );

class InitReacts(models.Model):
    value = models.CharField(max_length=100)

