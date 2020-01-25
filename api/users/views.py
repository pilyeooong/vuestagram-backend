from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model

from api.users.permissions import IsOwner
from api.users.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = User.objects.all()
    lookup_field = "id"
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()
