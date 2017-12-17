from django.contrib import admin
from django.utils import timezone
from .models import Post

def make_published(modeladmin, request, queryset):
    queryset.update(published_date=timezone.now())
make_published.short_description = "Publish selected posts"

class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'created_date', 'published_date']
    ordering = ['author', 'title', 'created_date', 'published_date']
    actions = [make_published]

admin.site.register(Post, PostAdmin)