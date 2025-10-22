from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class CommunityPost(models.Model):
    """
    Community forum posts for candidates to share experiences and learn.
    """
    POST_TYPE_CHOICES = [
        ('question', 'Question'),
        ('experience', 'Interview Experience'),
        ('advice', 'Career Advice'),
        ('discussion', 'Discussion'),
    ]
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='community_posts'
    )
    title = models.CharField(
        max_length=200,
        help_text=_('Post title')
    )
    content = models.TextField(
        help_text=_('Post content')
    )
    post_type = models.CharField(
        max_length=20,
        choices=POST_TYPE_CHOICES,
        default='discussion'
    )
    tags = models.JSONField(
        default=list,
        blank=True,
        help_text=_('Tags for categorization')
    )
    is_anonymous = models.BooleanField(
        default=False,
        help_text=_('Post anonymously')
    )
    is_pinned = models.BooleanField(
        default=False,
        help_text=_('Pin to top of community')
    )
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Community Post')
        verbose_name_plural = _('Community Posts')
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class CommunityComment(models.Model):
    """
    Comments on community posts.
    """
    post = models.ForeignKey(
        CommunityPost,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='community_comments'
    )
    content = models.TextField(
        help_text=_('Comment content')
    )
    is_anonymous = models.BooleanField(
        default=False,
        help_text=_('Comment anonymously')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Community Comment')
        verbose_name_plural = _('Community Comments')
        ordering = ['created_at']
    
    def __str__(self):
        return f"Comment on {self.post.title}"


class MentorshipRequest(models.Model):
    """
    Peer mentorship connections within the community.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
        ('completed', 'Completed'),
    ]
    
    mentee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='mentorship_requests_sent'
    )
    mentor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='mentorship_requests_received'
    )
    topic = models.CharField(
        max_length=200,
        help_text=_('Mentorship topic/area')
    )
    message = models.TextField(
        help_text=_('Introduction message')
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Mentorship Request')
        verbose_name_plural = _('Mentorship Requests')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.mentee.username} -> {self.mentor.username}: {self.topic}"


class ResourceShare(models.Model):
    """
    Shared resources and learning materials in the community.
    """
    RESOURCE_TYPE_CHOICES = [
        ('article', 'Article'),
        ('video', 'Video'),
        ('course', 'Course'),
        ('book', 'Book'),
        ('tool', 'Tool'),
        ('other', 'Other'),
    ]
    
    shared_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='shared_resources'
    )
    title = models.CharField(
        max_length=200,
        help_text=_('Resource title')
    )
    description = models.TextField(
        help_text=_('Resource description')
    )
    resource_type = models.CharField(
        max_length=20,
        choices=RESOURCE_TYPE_CHOICES
    )
    url = models.URLField(
        help_text=_('Resource URL')
    )
    tags = models.JSONField(
        default=list,
        blank=True,
        help_text=_('Tags for categorization')
    )
    upvotes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Resource Share')
        verbose_name_plural = _('Resource Shares')
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

