from rest_framework.routers import SimpleRouter
from .views import DropBoxViewset
from turtle import home
from django.urls import re_path
from .views import *
# router = SimpleRouter()
# router.register('accounts', DropBoxViewset)
# urlpatterns = router.urls
urlpatterns = [
    # re_path(r'upload',upload_resume),

    re_path(r'up', DropBoxViewset.as_view()),

    # re_path(r'verifyotp', VerifyOtp.as_view(), name='verifyotp')

]
