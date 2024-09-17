from django.urls import path
from .views import sign_up, activate, resend_verification_email
from .views import custom_login, verify_account, waiting_for_approval
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', sign_up, name='register'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('resend-verification/', resend_verification_email, name='resend_verification'),
    path('login/', custom_login, name='login'),
    path('verify-account/', verify_account, name='verify_account'),
    path('waiting-for-approval/', waiting_for_approval, name='waiting_for_approval'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # Make sure next_page redirects to 'home'
]
