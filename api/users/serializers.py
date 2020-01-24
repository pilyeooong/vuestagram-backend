from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'profile_image', 'gender', 
                  'introduction', 'following', 'followers']
