from django.urls import path
from .views import sign_up, activate, resend_verification_email

urlpatterns = [
    path('register/', sign_up, name='register'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('resend-verification/', resend_verification_email, name='resend_verification'),
]
