from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class ApplicationFeedback(models.Model):
    """
    Real-time feedback on applications.
    Mandatory personalization - no generic rejections allowed.
    """
    FEEDBACK_TYPE_CHOICES = [
        ('screening', 'Screening Feedback'),
        ('interview', 'Interview Feedback'),
        ('technical', 'Technical Assessment Feedback'),
        ('final', 'Final Decision Feedback'),
    ]
    
    application = models.ForeignKey(
        'candidates.Application',
        on_delete=models.CASCADE,
        related_name='feedback'
    )
    feedback_type = models.CharField(
        max_length=20,
        choices=FEEDBACK_TYPE_CHOICES
    )
    provided_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='feedback_given'
    )
    # Forced personalization - these fields are required
    strengths = models.TextField(
        help_text=_('Specific strengths observed (required for personalization)')
    )
    areas_for_improvement = models.TextField(
        help_text=_('Specific areas for growth (required for personalization)')
    )
    detailed_comments = models.TextField(
        help_text=_('Detailed, personalized feedback (required)')
    )
    # Optional fields
    rating = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text=_('Rating (1-5)')
    )
    next_steps = models.TextField(
        blank=True,
        help_text=_('Information about next steps in the process')
    )
    is_visible_to_candidate = models.BooleanField(
        default=True,
        help_text=_('Make feedback visible to candidate immediately')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Application Feedback')
        verbose_name_plural = _('Application Feedback')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Feedback for {self.application} - {self.feedback_type}"
    
    def save(self, *args, **kwargs):
        """
        Validate that personalization requirements are met.
        """
        if not self.strengths or len(self.strengths) < 50:
            raise ValueError("Strengths must be detailed (minimum 50 characters)")
        if not self.areas_for_improvement or len(self.areas_for_improvement) < 50:
            raise ValueError("Areas for improvement must be detailed (minimum 50 characters)")
        if not self.detailed_comments or len(self.detailed_comments) < 100:
            raise ValueError("Detailed comments must be comprehensive (minimum 100 characters)")
        super().save(*args, **kwargs)


class FeedbackResponse(models.Model):
    """
    Candidate responses to feedback (two-way communication).
    """
    feedback = models.ForeignKey(
        ApplicationFeedback,
        on_delete=models.CASCADE,
        related_name='responses'
    )
    response_text = models.TextField(
        help_text=_('Candidate response to feedback')
    )
    is_public = models.BooleanField(
        default=False,
        help_text=_('Share anonymously with community for learning')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Feedback Response')
        verbose_name_plural = _('Feedback Responses')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Response to {self.feedback}"


class FeedbackTemplate(models.Model):
    """
    Templates to help recruiters provide personalized feedback faster.
    Note: Templates are starting points - personalization still required.
    """
    name = models.CharField(
        max_length=200,
        help_text=_('Template name')
    )
    feedback_type = models.CharField(
        max_length=20,
        choices=ApplicationFeedback.FEEDBACK_TYPE_CHOICES
    )
    strengths_template = models.TextField(
        help_text=_('Template for strengths section (must be customized)')
    )
    improvement_template = models.TextField(
        help_text=_('Template for areas of improvement (must be customized)')
    )
    comments_template = models.TextField(
        help_text=_('Template for detailed comments (must be customized)')
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='feedback_templates'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Feedback Template')
        verbose_name_plural = _('Feedback Templates')
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.feedback_type})"

