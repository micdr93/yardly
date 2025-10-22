from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class AIDecisionLog(models.Model):
    """
    Transparent logging of all AI decisions for accountability.
    """
    DECISION_TYPE_CHOICES = [
        ('screening', 'Application Screening'),
        ('matching', 'Job Matching'),
        ('ranking', 'Candidate Ranking'),
        ('recommendation', 'Recommendation'),
    ]
    
    application = models.ForeignKey(
        'candidates.Application',
        on_delete=models.CASCADE,
        related_name='ai_decisions',
        blank=True,
        null=True
    )
    decision_type = models.CharField(
        max_length=20,
        choices=DECISION_TYPE_CHOICES
    )
    model_version = models.CharField(
        max_length=50,
        help_text=_('AI model version used')
    )
    input_data = models.JSONField(
        help_text=_('Input data used for decision (anonymized)')
    )
    output_data = models.JSONField(
        help_text=_('AI decision output')
    )
    confidence_score = models.FloatField(
        help_text=_('AI confidence in decision (0-1)')
    )
    explanation = models.TextField(
        help_text=_('Human-readable explanation of decision')
    )
    features_used = models.JSONField(
        default=list,
        help_text=_('Features/factors considered in decision')
    )
    human_reviewed = models.BooleanField(
        default=False,
        help_text=_('Whether decision was reviewed by human')
    )
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='ai_decisions_reviewed'
    )
    human_override = models.BooleanField(
        default=False,
        help_text=_('Whether human overrode AI decision')
    )
    override_reason = models.TextField(
        blank=True,
        help_text=_('Reason for human override')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('AI Decision Log')
        verbose_name_plural = _('AI Decision Logs')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"AI {self.decision_type} - {self.created_at}"


class BiasAuditLog(models.Model):
    """
    Regular bias audits of AI systems.
    """
    AUDIT_TYPE_CHOICES = [
        ('gender', 'Gender Bias Audit'),
        ('race', 'Racial Bias Audit'),
        ('age', 'Age Bias Audit'),
        ('location', 'Geographic Bias Audit'),
        ('education', 'Educational Background Bias Audit'),
        ('comprehensive', 'Comprehensive Bias Audit'),
    ]
    
    audit_type = models.CharField(
        max_length=20,
        choices=AUDIT_TYPE_CHOICES
    )
    audit_date = models.DateField(
        help_text=_('Date of audit')
    )
    model_version = models.CharField(
        max_length=50,
        help_text=_('AI model version audited')
    )
    sample_size = models.PositiveIntegerField(
        help_text=_('Number of decisions audited')
    )
    findings = models.TextField(
        help_text=_('Audit findings and observations')
    )
    bias_detected = models.BooleanField(
        default=False,
        help_text=_('Whether bias was detected')
    )
    bias_severity = models.CharField(
        max_length=20,
        choices=[
            ('none', 'None'),
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
            ('critical', 'Critical'),
        ],
        default='none'
    )
    corrective_actions = models.TextField(
        blank=True,
        help_text=_('Corrective actions taken or planned')
    )
    metrics = models.JSONField(
        default=dict,
        help_text=_('Detailed audit metrics and statistics')
    )
    audited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bias_audits_conducted'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Bias Audit Log')
        verbose_name_plural = _('Bias Audit Logs')
        ordering = ['-audit_date']
    
    def __str__(self):
        return f"{self.audit_type} - {self.audit_date}"


class EthicalAIGuideline(models.Model):
    """
    Documented ethical AI guidelines and principles.
    """
    title = models.CharField(
        max_length=200,
        help_text=_('Guideline title')
    )
    description = models.TextField(
        help_text=_('Detailed guideline description')
    )
    principle = models.CharField(
        max_length=100,
        help_text=_('Core ethical principle (e.g., Fairness, Transparency)')
    )
    implementation_details = models.TextField(
        help_text=_('How this guideline is implemented')
    )
    version = models.CharField(
        max_length=20,
        help_text=_('Guideline version')
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_('Whether guideline is currently active')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Ethical AI Guideline')
        verbose_name_plural = _('Ethical AI Guidelines')
        ordering = ['principle', 'title']
    
    def __str__(self):
        return f"{self.title} (v{self.version})"


class DataPrivacyLog(models.Model):
    """
    Log of data access and usage for privacy compliance.
    """
    ACCESS_TYPE_CHOICES = [
        ('view', 'Data Viewed'),
        ('export', 'Data Exported'),
        ('delete', 'Data Deleted'),
        ('anonymize', 'Data Anonymized'),
        ('ai_training', 'Used in AI Training'),
    ]
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='data_access_logs'
    )
    accessed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='data_accesses_made'
    )
    access_type = models.CharField(
        max_length=20,
        choices=ACCESS_TYPE_CHOICES
    )
    data_type = models.CharField(
        max_length=100,
        help_text=_('Type of data accessed')
    )
    purpose = models.TextField(
        help_text=_('Purpose of data access')
    )
    consent_given = models.BooleanField(
        default=False,
        help_text=_('Whether user consent was obtained')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('Data Privacy Log')
        verbose_name_plural = _('Data Privacy Logs')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.access_type} - {self.user.username} by {self.accessed_by.username}"

