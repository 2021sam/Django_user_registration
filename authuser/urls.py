from django.contrib import admin
from django.urls import path, include
from user.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Root URL points to the home view
    path('user/', include('user.urls')),  # Include the user app's URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Include the built-in auth views
]
