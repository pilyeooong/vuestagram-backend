from rest_framework import serializers
from apps.posts.models import Post
from apps.posts.models import Comment


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'author', 'photo', 'location', 'caption',
                  'like_count', 'comment_count', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    
    author = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'comment', 'author', 'created_at', 'updated_at']
