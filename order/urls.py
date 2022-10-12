from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'order', OrderView.as_view()),
    # re_path(r'verifyotp', VerifyOtp.as_view(), name='verifyotp')

]
