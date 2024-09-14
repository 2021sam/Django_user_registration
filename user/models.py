# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = None  # Remove the default username field
    email = models.EmailField(unique=True)  # Set email field to be unique and required

    USERNAME_FIELD = 'email'  # Set the email field as the identifier for the user
    REQUIRED_FIELDS = []  # Remove the default 'username' from required fields
