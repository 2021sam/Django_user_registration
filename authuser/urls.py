# /Users/2021sam/apps/authuser/authuser/urls.py
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from user.views import home, custom_login
from user import views as user_views

urlpatterns = [
    path('', home, name='home'),  # Root URL points to the home view
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),  # Include user app URLs
    path('accounts/login/', custom_login, name='login'),  # Override the default login view
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's built-in authentication views for the other routes
        # Logout URL
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Profile page
    path('profile/', user_views.profile, name='profile'),
]
