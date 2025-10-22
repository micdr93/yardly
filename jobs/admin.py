from django.contrib import admin
from .models import Company, JobPosting


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Company admin."""
    list_display = ('name', 'industry', 'size', 'location', 'created_at')
    list_filter = ('industry', 'size')
    search_fields = ('name', 'industry', 'location')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    """Job posting admin."""
    list_display = ('title', 'company', 'location', 'remote_type', 'employment_type', 
                   'status', 'created_at')
    list_filter = ('status', 'remote_type', 'employment_type', 'created_at')
    search_fields = ('title', 'company__name', 'location')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'

