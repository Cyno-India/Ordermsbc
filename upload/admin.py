from django.contrib import admin

# Register your models here.
from .models import Docs, MasterDocs
admin.site.register(Docs)
admin.site.register(MasterDocs)

