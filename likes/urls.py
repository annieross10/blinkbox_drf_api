from django.urls import path
from likes import views

urlpatterns = [
    path('likes/', views.LikeCreateAPIView.as_view()),
    path('loves/', views.LoveCreateAPIView.as_view()),
    path('laughs/', views.LaughCreateAPIView.as_view()),
]