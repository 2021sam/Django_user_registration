from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Create a CustomUserAdmin class to manage how the user model appears in the admin
class CustomUserAdmin(UserAdmin):
    # Specify the fields to display in the admin interface
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    
    # Fields that can be searched in the admin
    search_fields = ('email', 'first_name', 'last_name')

    # Custom form to add and edit users
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    
    # Specify the fields that are shown when viewing or editing users
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Email as the unique identifier instead of username
    ordering = ('email',)

# Register the CustomUser model with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
