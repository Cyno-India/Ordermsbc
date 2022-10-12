from django.db import models

# Create your models here.
from orderplacementapi.models import *

class Order(models.Model):
    customer_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default="")
    orderfile = models.FileField()
    