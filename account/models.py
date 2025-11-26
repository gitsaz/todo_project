from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManagerForm
# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        max_length=50,
        unique=True
    )
    email = models.EmailField(
        max_length=100,
        unique=True
    )
    
    
    REQUIRED_FIELDS = ['email']
    objects = UserManagerForm()
    
    def __str__(self):
        return self.username