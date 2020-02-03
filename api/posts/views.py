from rest_framework import viewsets
from rest_framework import status
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from api.users.serializers import UserSerializer
from api.posts.serializers import CommentSerializer
from api.posts.serializers import PostSerializer
from apps.posts.models import Comment
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
    def get(self, request, post_id):
        likes = Like.objects.filter(post__id=post_id)
        like_author_id = likes.values('author_id')
        users = User.objects.filter(id__in=like_author_id)

        serializer = UserSerializer(users, many=True,
                                    context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, post_id):
        user = request.user

        try:
            post_exist = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            like_check = Like.objects.get(
                author=user,
                post=post_exist
            )
            if like_check:
                return Response(status=status.HTTP_304_NOT_MODIFIED)

        except Like.DoesNotExist:
            add_like = Like.objects.create(
                author=user,
                post=post_exist
            )
            add_like.save()

            return Response(status=status.HTTP_201_CREATED)


class UnLikePost(APIView):
    def delete(self, request, post_id):
        user = request.user

        try:
            like_exist = Like.objects.get(
                author=user,
                post__id=post_id
            )
            like_exist.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Like.DoesNotExist:
            return Response(status=status.HTTP_304_NOT_MODIFIED)


class AddComment(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=kwarg_id)

        if post.comments.filter(author=request_user).exists():
            raise ValidationError("You have already answered this Post !")
        serializer.save(author=self.request.user, post=post)


class CommentList(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post__id=kwarg_id).order_by('-created_at')
    

class CommentRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
