# views.py

from django.db.models import Count
from rest_framework import generics, filters
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(posts_count=Count('owner__post', distinct=True))
    serializer_class = ProfileSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['owner__username']  # Assuming you want to search by owner's username
    ordering_fields = ['created_at']  # Assuming you want to order by profile creation date

class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(posts_count=Count('owner__post', distinct=True))
    serializer_class = ProfileSerializer
