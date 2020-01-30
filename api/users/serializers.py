from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    if_follow = serializers.SerializerMethodField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'profile_image', 'gender',
                  'introduction', 'followers_count', 'following_count',
                  'if_follow', 'following', 'followers']

    # 로그인 유저가 다른 유저를 팔로우하고 있는지 체크
    def get_if_follow(self, obj):
        if 'request' in self.context:
            request = self.context['request']
            if obj in request.user.following.all():
                return True
        return False
