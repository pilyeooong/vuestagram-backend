from django.contrib import admin

from .models import Post
from .models import Like
from .models import Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ['location', 'author']
    list_display = ['id', 'author', 'photo', 'location', 'caption']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['author', 'photo']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'photo', 'comment', 'created_at', 'updated_at']
