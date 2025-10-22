from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserPreferences


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Custom user admin."""
    list_display = ('username', 'email', 'user_type', 'first_name', 'last_name', 'is_staff')
    list_filter = ('user_type', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Yardly Profile', {
            'fields': ('user_type', 'profile_picture', 'bio', 'phone_number', 
                      'location', 'linkedin_url', 'github_url', 'portfolio_url')
        }),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Yardly Profile', {
            'fields': ('user_type',)
        }),
    )


@admin.register(UserPreferences)
class UserPreferencesAdmin(admin.ModelAdmin):
    """User preferences admin."""
    list_display = ('user', 'receive_email_notifications', 'real_time_feedback_enabled', 
                   'community_visibility')
    list_filter = ('receive_email_notifications', 'real_time_feedback_enabled', 
                  'community_visibility')
    search_fields = ('user__username', 'user__email')

