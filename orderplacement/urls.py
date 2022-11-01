"""orderplacement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path , include
from django.conf.urls.static import static
from rest_framework import routers
from order import views

router = routers.DefaultRouter()
router.register(r'file', views.FileUploadViewSet, basename='file')

urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'api/user/', include('orderplacementapi.urls')),
    re_path(r'api/order/', include('order.urls')),
    re_path(r'upload/', include(router.urls)),
    # re_path(r'api/uploader', include('upload.urls')),
   re_path(r'apii/', include('rest_framework.urls')),  # new
    re_path(r'api/upload/', include('upload.urls')),  #
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)