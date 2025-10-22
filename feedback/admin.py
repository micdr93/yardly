from django.contrib import admin
from .models import ApplicationFeedback, FeedbackResponse, FeedbackTemplate


@admin.register(ApplicationFeedback)
class ApplicationFeedbackAdmin(admin.ModelAdmin):
    """Application feedback admin."""
    list_display = ('application', 'feedback_type', 'provided_by', 'is_visible_to_candidate', 
                   'rating', 'created_at')
    list_filter = ('feedback_type', 'is_visible_to_candidate', 'rating', 'created_at')
    search_fields = ('application__candidate__username', 'application__job__title', 
                    'provided_by__username')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(FeedbackResponse)
class FeedbackResponseAdmin(admin.ModelAdmin):
    """Feedback response admin."""
    list_display = ('feedback', 'is_public', 'created_at')
    list_filter = ('is_public', 'created_at')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(FeedbackTemplate)
class FeedbackTemplateAdmin(admin.ModelAdmin):
    """Feedback template admin."""
    list_display = ('name', 'feedback_type', 'created_by', 'is_active', 'created_at')
    list_filter = ('feedback_type', 'is_active', 'created_at')
    search_fields = ('name', 'created_by__username')
    readonly_fields = ('created_at', 'updated_at')

