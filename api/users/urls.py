from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.users.views import UserViewSet
from api.users.views import FollowUser
from api.users.views import UnFollowUser

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/<int:id>/follow/', FollowUser.as_view(), name='follow-user'),
    path('users/<int:id>/unfollow/', UnFollowUser.as_view(),
         name='unfollow-user'),
]
