from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Custom user model for Yardly platform.
    Supports both candidates and recruiters with different roles.
    """
    USER_TYPE_CHOICES = (
        ('candidate', 'Candidate'),
        ('recruiter', 'Recruiter'),
        ('admin', 'Admin'),
    )
    
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default='candidate',
        help_text=_('Type of user account')
    )
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True,
        help_text=_('User profile picture')
    )
    bio = models.TextField(
        blank=True,
        help_text=_('User biography')
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        help_text=_('Contact phone number')
    )
    location = models.CharField(
        max_length=100,
        blank=True,
        help_text=_('User location')
    )
    linkedin_url = models.URLField(
        blank=True,
        help_text=_('LinkedIn profile URL')
    )
    github_url = models.URLField(
        blank=True,
        help_text=_('GitHub profile URL')
    )
    portfolio_url = models.URLField(
        blank=True,
        help_text=_('Portfolio website URL')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"


class UserPreferences(models.Model):
    """
    User preferences for personalization features.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='preferences'
    )
    receive_email_notifications = models.BooleanField(
        default=True,
        help_text=_('Receive email notifications')
    )
    receive_sms_notifications = models.BooleanField(
        default=False,
        help_text=_('Receive SMS notifications')
    )
    real_time_feedback_enabled = models.BooleanField(
        default=True,
        help_text=_('Enable real-time feedback notifications')
    )
    community_visibility = models.BooleanField(
        default=True,
        help_text=_('Make profile visible in community')
    )
    share_anonymous_feedback = models.BooleanField(
        default=True,
        help_text=_('Share anonymized feedback to help improve the platform')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('User Preference')
        verbose_name_plural = _('User Preferences')
    
    def __str__(self):
        return f"Preferences for {self.user.username}"

