from django.urls import path
from .views import sign_up, activate, resend_verification_email
from .views import custom_login, verify_account

urlpatterns = [
    path('register/', sign_up, name='register'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('resend-verification/', resend_verification_email, name='resend_verification'),
    path('login/', custom_login, name='login'),
    path('verify-account/', verify_account, name='verify_account'),
]
