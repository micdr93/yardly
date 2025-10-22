from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    """
    Company profile for recruiters.
    """
    name = models.CharField(
        max_length=200,
        help_text=_('Company name')
    )
    description = models.TextField(
        help_text=_('Company description')
    )
    website = models.URLField(
        blank=True,
        help_text=_('Company website')
    )
    logo = models.ImageField(
        upload_to='company_logos/',
        blank=True,
        null=True,
        help_text=_('Company logo')
    )
    industry = models.CharField(
        max_length=100,
        blank=True,
        help_text=_('Industry sector')
    )
    size = models.CharField(
        max_length=50,
        choices=[
            ('1-10', '1-10 employees'),
            ('11-50', '11-50 employees'),
            ('51-200', '51-200 employees'),
            ('201-500', '201-500 employees'),
            ('501-1000', '501-1000 employees'),
            ('1001+', '1001+ employees'),
        ],
        blank=True,
        help_text=_('Company size')
    )
    location = models.CharField(
        max_length=200,
        blank=True,
        help_text=_('Headquarters location')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')
        ordering = ['name']
    
    def __str__(self):
        return self.name


class JobPosting(models.Model):
    """
    Job posting with forced personalization and transparency.
    """
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('paused', 'Paused'),
        ('closed', 'Closed'),
    ]
    
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='job_postings'
    )
    recruiter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posted_jobs'
    )
    title = models.CharField(
        max_length=200,
        help_text=_('Job title')
    )
    description = models.TextField(
        help_text=_('Detailed job description')
    )
    responsibilities = models.TextField(
        help_text=_('Key responsibilities')
    )
    requirements = models.TextField(
        help_text=_('Required qualifications and skills')
    )
    preferred_qualifications = models.TextField(
        blank=True,
        help_text=_('Preferred qualifications (nice to have)')
    )
    location = models.CharField(
        max_length=200,
        help_text=_('Job location')
    )
    remote_type = models.CharField(
        max_length=20,
        choices=[
            ('remote', 'Remote'),
            ('hybrid', 'Hybrid'),
            ('onsite', 'On-site'),
        ],
        default='onsite'
    )
    employment_type = models.CharField(
        max_length=20,
        choices=[
            ('full_time', 'Full Time'),
            ('part_time', 'Part Time'),
            ('contract', 'Contract'),
            ('internship', 'Internship'),
        ],
        default='full_time'
    )
    salary_min = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text=_('Minimum salary (transparency required)')
    )
    salary_max = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text=_('Maximum salary (transparency required)')
    )
    salary_currency = models.CharField(
        max_length=3,
        default='USD',
        help_text=_('Currency code (e.g., USD, EUR, GBP)')
    )
    benefits = models.TextField(
        blank=True,
        help_text=_('Benefits and perks')
    )
    skills_required = models.JSONField(
        default=list,
        help_text=_('Required skills list')
    )
    skills_preferred = models.JSONField(
        default=list,
        blank=True,
        help_text=_('Preferred skills list')
    )
    experience_min = models.PositiveIntegerField(
        default=0,
        help_text=_('Minimum years of experience')
    )
    experience_max = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text=_('Maximum years of experience')
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )
    application_deadline = models.DateField(
        blank=True,
        null=True,
        help_text=_('Application deadline')
    )
    # Forced personalization fields
    requires_cover_letter = models.BooleanField(
        default=True,
        help_text=_('Require personalized cover letter')
    )
    custom_questions = models.JSONField(
        default=list,
        blank=True,
        help_text=_('Custom application questions')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Job Posting')
        verbose_name_plural = _('Job Postings')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} at {self.company.name}"

