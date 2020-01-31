from rest_framework import serializers
from apps.posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'photo', 'location', 'caption',
                  'like_count', 'created_at', 'updated_at']

