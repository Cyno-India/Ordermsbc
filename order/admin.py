from django.contrib import admin
from .models import FileUpload, MasterModel, Order

# Register your models here.
admin.site.register(Order)
admin.site.register(MasterModel)
admin.site.register(FileUpload)


