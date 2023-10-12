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

