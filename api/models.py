from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=240,unique=True)
    password=models.CharField(max_length=200)
    username=models.CharField(max_length=200)

    # set email as default
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

