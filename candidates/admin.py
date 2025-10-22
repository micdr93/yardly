from django.contrib import admin
from .models import CandidateProfile, Application


@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):
    """Candidate profile admin."""
    list_display = ('user', 'current_title', 'years_of_experience', 'remote_preference', 'created_at')
    list_filter = ('remote_preference', 'willing_to_relocate')
    search_fields = ('user__username', 'user__email', 'current_title', 'current_company')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    """Application admin."""
    list_display = ('candidate', 'job', 'status', 'submitted_at', 'ai_match_score')
    list_filter = ('status', 'submitted_at')
    search_fields = ('candidate__username', 'job__title')
    readonly_fields = ('created_at', 'updated_at', 'last_status_change')
    date_hierarchy = 'submitted_at'

