from rest_framework.routers import DefaultRouter

from django.urls import include
from django.urls import path

from api.posts.views import PostViewSet
from api.posts.views import LikePost
from api.posts.views import UnLikePost

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:id>/like/', LikePost.as_view(), name="like-post"),
    path('posts/<int:id>/unlike/', UnLikePost.as_view(), name="UnLike-post"),
]