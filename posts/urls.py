from django.urls import path
from posts import views
from .views import PostLike, PostLove, PostLaugh

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('likes/<int:pk>/', PostLike.as_view(), name='post_like'),
    path('loves/<int:pk>/', PostLove.as_view(), name='post_love'),
    path('laughs/<int:pk>/', PostLaugh.as_view(), name='post_laugh'),
]