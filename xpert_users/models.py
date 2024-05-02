from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    """defines user objects"""
    USER = {
        "Service provider": "Service provider",
        "Service seeker": "Service seeker",
    }

    GENDER = {
        "M": "Male",
        "F": "Female", 
    }
    account_type = models.CharField(max_length=30, choices=USER)
    gender = models.CharField(max_length=1, choices=GENDER)
    profile_picture = models.ImageField(default="default.jpg", upload_to="profile_pictures")
    profession = models.CharField(max_length=150, null=True, blank=True)
    about_me = models.CharField(max_length=500, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    town = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    available = models.BooleanField(default=True)
    
    def __str__(self):
        """formats string representation"""
        return self.username


# class UserProfiles(models.Model):
#     """defines profiles for each user account"""
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_picture = models.ImageField(default="default.jpg", upload_to="profile_pictures")
#     profession = models.CharField(max_length=150, null=False, blank=False)
#     about_me = models.CharField(max_length=500, null=False, blank=False)
#     region = models.CharField(max_length=100, null=False, blank=False)
#     town = models.CharField(max_length=100, null=False, blank=False)
#     phone = models.CharField(max_length=15)
#     available = models.BooleanField(default=True)

#     def __str__(self):
#         """formats string representation"""
#         return self.user.username