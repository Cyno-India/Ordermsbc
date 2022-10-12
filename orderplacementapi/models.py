from operator import mod
from pyexpat import model
from django.db import models

from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('customer', 'Customer')
    )
    email = models.EmailField(null=True, unique=True)
    phone = models.CharField(max_length=10, null=True , unique=True)
    username = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(choices=ROLES, max_length=10)

    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

