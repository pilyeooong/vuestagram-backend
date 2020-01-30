from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from api.users.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    lookup_field = "id"
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class FollowUser(APIView):
    def post(self, request, id):
        user = request.user
        try:
            user_to_follow = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.following.add(user_to_follow)
        user.save()

        return Response(status=status.HTTP_200_OK)


class UnFollowUser(APIView):
    def post(self, request, id):
        user = request.user
        try:
            user_to_unfollow = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.following.remove(user_to_unfollow)
        user.save()

        return Response(status=status.HTTP_200_OK)
