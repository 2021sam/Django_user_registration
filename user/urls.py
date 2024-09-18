# /Users/2021sam/apps/authuser/user/urls.py
from django.urls import path
from .views import sign_up, activate, resend_verification_email
from .views import custom_login, verify_account, waiting_for_approval, delete_account
from django.contrib.auth import views as auth_views
from .views import check_verification_status


urlpatterns = [
    path('register/', sign_up, name='register'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('resend-verification/', resend_verification_email, name='resend_verification'),
    path('login/', custom_login, name='login'),
    path('verify-account/', verify_account, name='verify_account'),
    path('waiting-for-approval/', waiting_for_approval, name='waiting_for_approval'),
    path('check-verification-status/', check_verification_status, name='check_verification_status'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # Make sure next_page redirects to 'home'
    path('delete_account/', delete_account, name='delete_account'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),



]
