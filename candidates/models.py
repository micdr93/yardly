from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class CandidateProfile(models.Model):
    """
    Extended profile for candidates with detailed information.
    Candidate-first approach: comprehensive, privacy-conscious profile.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='candidate_profile'
    )
    resume = models.FileField(
        upload_to='resumes/',
        blank=True,
        null=True,
        help_text=_('Upload your resume (PDF, DOC, DOCX)')
    )
    cover_letter = models.TextField(
        blank=True,
        help_text=_('Default cover letter')
    )
    years_of_experience = models.PositiveIntegerField(
        default=0,
        help_text=_('Total years of professional experience')
    )
    current_title = models.CharField(
        max_length=200,
        blank=True,
        help_text=_('Current job title')
    )
    current_company = models.CharField(
        max_length=200,
        blank=True,
        help_text=_('Current employer')
    )
    salary_expectation_min = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text=_('Minimum salary expectation')
    )
    salary_expectation_max = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text=_('Maximum salary expectation')
    )
    preferred_locations = models.JSONField(
        default=list,
        blank=True,
        help_text=_('List of preferred work locations')
    )
    remote_preference = models.CharField(
        max_length=20,
        choices=[
            ('remote', 'Remote Only'),
            ('hybrid', 'Hybrid'),
            ('onsite', 'On-site'),
            ('flexible', 'Flexible'),
        ],
        default='flexible',
        help_text=_('Work location preference')
    )
    availability_date = models.DateField(
        blank=True,
        null=True,
        help_text=_('Date available to start')
    )
    skills = models.JSONField(
        default=list,
        blank=True,
        help_text=_('List of skills')
    )
    languages = models.JSONField(
        default=list,
        blank=True,
        help_text=_('Languages spoken with proficiency levels')
    )
    certifications = models.JSONField(
        default=list,
        blank=True,
        help_text=_('Professional certifications')
    )
    education = models.JSONField(
        default=list,
        blank=True,
        help_text=_('Educational background')
    )
    work_authorization = models.CharField(
        max_length=100,
        blank=True,
        help_text=_('Work authorization status')
    )
    willing_to_relocate = models.BooleanField(
        default=False,
        help_text=_('Willing to relocate for the right opportunity')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Candidate Profile')
        verbose_name_plural = _('Candidate Profiles')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Profile: {self.user.username}"


class Application(models.Model):
    """
    Job application with candidate-first tracking and transparency.
    """
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('screening', 'Screening'),
        ('interviewing', 'Interviewing'),
        ('offer', 'Offer Extended'),
        ('accepted', 'Offer Accepted'),
        ('rejected', 'Rejected'),
        ('withdrawn', 'Withdrawn'),
    ]
    
    candidate = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    job = models.ForeignKey(
        'jobs.JobPosting',
        on_delete=models.CASCADE,
        related_name='applications'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )
    cover_letter = models.TextField(
        help_text=_('Personalized cover letter for this application')
    )
    resume = models.FileField(
        upload_to='application_resumes/',
        blank=True,
        null=True,
        help_text=_('Custom resume for this application')
    )
    additional_documents = models.JSONField(
        default=list,
        blank=True,
        help_text=_('Additional documents attached to application')
    )
    submitted_at = models.DateTimeField(
        blank=True,
        null=True,
        help_text=_('When the application was submitted')
    )
    last_status_change = models.DateTimeField(
        auto_now=True,
        help_text=_('Last time status was updated')
    )
    ai_match_score = models.FloatField(
        blank=True,
        null=True,
        help_text=_('AI-calculated match score (transparent to candidate)')
    )
    ai_match_explanation = models.TextField(
        blank=True,
        help_text=_('Explanation of AI match score (ethical AI)')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Application')
        verbose_name_plural = _('Applications')
        ordering = ['-submitted_at']
        unique_together = ['candidate', 'job']
    
    def __str__(self):
        return f"{self.candidate.username} - {self.job.title} ({self.status})"

