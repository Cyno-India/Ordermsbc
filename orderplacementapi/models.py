from distutils.command.upload import upload
from email.policy import default
from operator import mod
from pyexpat import model
from random import choices
from django.db import models

from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('customer', 'Customer')
    )
    ALLOWED_COUNTRIES = (
        ('japan','Japan'),
        ('france','France'),
        ('germany','Germany'),
        ('china','China')
    )
    email = models.EmailField(null=True, unique=True)
    phone = models.CharField(max_length=10, null=True , unique=True)
    username = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(choices=ROLES, max_length=10)
    country = models.CharField(choices=ALLOWED_COUNTRIES, max_length=10, default="")


    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

