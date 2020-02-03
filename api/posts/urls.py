from rest_framework.routers import DefaultRouter

from django.urls import include
from django.urls import path

from api.posts.views import PostViewSet
from api.posts.views import LikePost
from api.posts.views import UnLikePost
from api.posts.views import AddComment
from api.posts.views import CommentList
from api.posts.views import CommentRUD

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/like/', LikePost.as_view(), name='like-post'),
    path('posts/<int:post_id>/unlike/', UnLikePost.as_view(), name='UnLike-post'),
    path('posts/<int:post_id>/comment/', AddComment.as_view(), name='add-comment'),
    path('posts/<int:post_id>/comments/', CommentList.as_view(), name='comment-list'),
    path('comment/<int:pk>/', CommentRUD.as_view(), name="comment-update"),
]
