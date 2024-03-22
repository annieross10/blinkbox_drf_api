from rest_framework import generics, permissions, status
from rest_framework.response import Response
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Like, Love, Laugh
from .serializers import LikeSerializer, LoveSerializer, LaughSerializer

class LikeListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

class LoveListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LoveSerializer
    queryset = Love.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LoveDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LoveSerializer
    queryset = Love.objects.all()

class LaughListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LaughSerializer
    queryset = Laugh.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LaughDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LaughSerializer
    queryset = Laugh.objects.all()
