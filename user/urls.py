from django.urls import path
from .views import sign_up, activate

urlpatterns = [
    path('register/', sign_up, name='register'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),  # Make sure it's uidb64, not uid
]
