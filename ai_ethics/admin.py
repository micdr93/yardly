from django.contrib import admin
from .models import AIDecisionLog, BiasAuditLog, EthicalAIGuideline, DataPrivacyLog


@admin.register(AIDecisionLog)
class AIDecisionLogAdmin(admin.ModelAdmin):
    """AI decision log admin."""
    list_display = ('decision_type', 'model_version', 'confidence_score', 'human_reviewed', 
                   'human_override', 'created_at')
    list_filter = ('decision_type', 'human_reviewed', 'human_override', 'created_at')
    search_fields = ('model_version', 'explanation')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'


@admin.register(BiasAuditLog)
class BiasAuditLogAdmin(admin.ModelAdmin):
    """Bias audit log admin."""
    list_display = ('audit_type', 'audit_date', 'model_version', 'bias_detected', 
                   'bias_severity', 'audited_by')
    list_filter = ('audit_type', 'bias_detected', 'bias_severity', 'audit_date')
    search_fields = ('model_version', 'findings', 'audited_by__username')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'audit_date'


@admin.register(EthicalAIGuideline)
class EthicalAIGuidelineAdmin(admin.ModelAdmin):
    """Ethical AI guideline admin."""
    list_display = ('title', 'principle', 'version', 'is_active', 'created_at')
    list_filter = ('principle', 'is_active', 'created_at')
    search_fields = ('title', 'principle', 'description')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(DataPrivacyLog)
class DataPrivacyLogAdmin(admin.ModelAdmin):
    """Data privacy log admin."""
    list_display = ('user', 'accessed_by', 'access_type', 'data_type', 'consent_given', 
                   'created_at')
    list_filter = ('access_type', 'consent_given', 'created_at')
    search_fields = ('user__username', 'accessed_by__username', 'data_type', 'purpose')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'

