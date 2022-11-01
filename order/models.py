from distutils.command import upload
from email.policy import default

from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.
from orderplacementapi.models import *

class Order(models.Model): 
    customer_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default="")
    file_name = models.CharField(max_length=10,default="")
    particular = models.CharField(max_length=50,default="")
    itemcode = models.CharField(max_length=10,default="")
    base_item_code = models.CharField(max_length=10,default="")
    qty = models.CharField(max_length=10,default="")
    cust = models.CharField(max_length=10,default="")
    address = models.CharField(max_length=50,default="")
    ship_by = models.CharField(max_length=10,default="RAM")
    consignee = models.CharField(max_length=10,default="")
    country = models.CharField(max_length=10,default="")
    phone = models.CharField(max_length=20,default="")
    pincode = models.CharField(max_length=10,default="")


class FileUpload(models.Model):
    # customer_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default="")
    file = models.FileField()



    # def save(self):
    #     #Generate a new license file overwriting any previous version
    #     #and update file path
    #     self.license_file.save(orderfile, new_contents)



class MasterModel(models.Model):
    Particular = models.CharField(max_length=50,default="")
    Ordered_ItemCode = models.CharField(max_length=20,default="")
    Base_ItemCode = models.CharField(max_length=20,default="")
    Qty = models.CharField(max_length=20,default="")