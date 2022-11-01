from django.urls import re_path
from .views import *
urlpatterns = [
    re_path(r'customerregister', CustomerRegisterView.as_view(), name='customer'),
    re_path(r'adminregister', AdminRegisterView.as_view()),
    re_path(r'Adminview', AdminView.as_view()),
    # re_path(r'Adminview', AdminViewPortal.as_view()),
    re_path(r'cookie', getcookie.as_view(), name='get'),

    re_path(r'login', LoginView.as_view(), name='login'),
    re_path(r'logout', LogoutView.as_view(), name='logout'),
    re_path(r'profile', UserProfileView.as_view(), name='profile'),
    # re_path(r'verifyotp', VerifyOtp.as_view(), name='verifyotp')

]
