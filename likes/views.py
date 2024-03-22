
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Like, Love, Laugh
from .serializers import LikeSerializer, LoveSerializer, LaughSerializer

class LikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

class LoveList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LoveSerializer

    def get_queryset(self):
        return Love.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LoveDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LoveSerializer
    queryset = Love.objects.all()

class LaughList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LaughSerializer

    def get_queryset(self):
        return Laugh.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LaughDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LaughSerializer
    queryset = Laugh.objects.all()
