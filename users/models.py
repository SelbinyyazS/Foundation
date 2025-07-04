from django.db import models

# Create your models here.
# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom User model that extends Django's default AbstractUser.
    We can add more fields here later, like a bio or profile picture.
    For now, we'll just use the fields from AbstractUser.
    The 'pass' statement means we're not adding any *new* fields yet.
    """

    email = models.EmailField(unique=True)
    # You could add new fields here in the future, for example:
    # bio = models.TextField(blank=True)
    # profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)