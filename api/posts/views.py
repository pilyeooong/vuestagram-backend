from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


from api.posts.serializers import PostSerializer
from apps.posts.models import Post
from apps.posts.models import Like

from django.contrib.auth import get_user_model

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    lookup_field = 'id'
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class LikePost(APIView):
    def post(self, request, id):
        user = request.user

        try:
            photo_exist = Post.objects.get(id=id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            like_check = Like.objects.get(
                author=user,
                photo=photo_exist
            )
            if(like_check):
                return Response(status=status.HTTP_304_NOT_MODIFIED)

        except Like.DoesNotExist:
            add_like = Like.objects.create(
                author=user,
                photo=photo_exist
            )
            add_like.save()

            return Response(status=status.HTTP_201_CREATED)


class UnLikePost(APIView):
    def delete(self, request, id):
        user = request.user

        try:
            like_exist = Like.objects.get(
                author=user,
                photo__id=id
            )
            like_exist.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Like.DoesNotExist:
            return Response(status=status.HTTP_304_NOT_MODIFIED)
