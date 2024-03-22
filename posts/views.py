from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        savedpost_count=Count('savedpost', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'likes_count',
        'likes__created_at',
        'savedpost_count'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        savedpost_count=Count('savedpost', distinct=True)
    ).order_by('-created_at')

class PostAction(generics.RetrieveUpdateDestroyAPIView):
    action_field = None

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        if hasattr(post, self.action_field):
            action_field = getattr(post, self.action_field)
            if action_field.filter(id=user.id).exists():
                action_field.remove(user)
            else:
                action_field.add(user)

        return HttpResponseRedirect(reverse('post_detail', args=[pk]))

class PostLike(PostAction):
    action_field = 'like'

class PostLove(PostAction):
    action_field = 'love'

class PostLaugh(PostAction):
    action_field = 'laugh'