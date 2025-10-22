from django.contrib import admin
from .models import CommunityPost, CommunityComment, MentorshipRequest, ResourceShare


@admin.register(CommunityPost)
class CommunityPostAdmin(admin.ModelAdmin):
    """Community post admin."""
    list_display = ('title', 'author', 'post_type', 'is_anonymous', 'is_pinned', 
                   'view_count', 'created_at')
    list_filter = ('post_type', 'is_anonymous', 'is_pinned', 'created_at')
    search_fields = ('title', 'content', 'author__username')
    readonly_fields = ('view_count', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(CommunityComment)
class CommunityCommentAdmin(admin.ModelAdmin):
    """Community comment admin."""
    list_display = ('post', 'author', 'is_anonymous', 'created_at')
    list_filter = ('is_anonymous', 'created_at')
    search_fields = ('content', 'author__username', 'post__title')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(MentorshipRequest)
class MentorshipRequestAdmin(admin.ModelAdmin):
    """Mentorship request admin."""
    list_display = ('mentee', 'mentor', 'topic', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('mentee__username', 'mentor__username', 'topic')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(ResourceShare)
class ResourceShareAdmin(admin.ModelAdmin):
    """Resource share admin."""
    list_display = ('title', 'shared_by', 'resource_type', 'upvotes', 'created_at')
    list_filter = ('resource_type', 'created_at')
    search_fields = ('title', 'description', 'shared_by__username')
    readonly_fields = ('upvotes', 'created_at', 'updated_at')

