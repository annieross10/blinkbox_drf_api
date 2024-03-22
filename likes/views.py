
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Like, Love, Laugh
from .serializers import LikeSerializer, LoveSerializer, LaughSerializer

class LikeCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LoveCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LoveSerializer
    queryset = Love.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LaughCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LaughSerializer
    queryset = Laugh.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

