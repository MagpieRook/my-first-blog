from django.contrib import admin
from django.utils import timezone
from .models import Post, Comment

def make_published(modeladmin, request, queryset):
    queryset.update(published_date=timezone.now())
make_published.short_description = "Publish selected posts"

class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'created_date', 'published_date']
    ordering = ['published_date', 'created_date']
    actions = [make_published]

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'created_date', 'approved_comment']
    ordering = ['created_date', 'approved_comment']
    actions = []

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)