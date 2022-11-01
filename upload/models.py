from django.db import models
from orderplacementapi.models import CustomUser
# Create your models here. 
class Docs(models.Model):
    customer_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default="")
    document = models.FileField(max_length=100)


class MasterDocs(models.Model):
    document = models.FileField(max_length=100)