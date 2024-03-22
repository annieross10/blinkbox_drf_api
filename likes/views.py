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

class PostUpdateAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        item_type = kwargs.get('item_type') 
        if item_type == 'like':
            # Handle update logic for the Like model
            # For example:
            like_id = request.data.get('like_id')
            like = Like.objects.get(id=like_id)
            serializer = LikeSerializer(like, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif item_type == 'love':
            # Handle update logic for the Love model
            pass
        elif item_type == 'laugh':
            # Handle update logic for the Laugh model
            pass
        else:
            return Response({"error": "Invalid item type"}, status=status.HTTP_400_BAD_REQUEST)
