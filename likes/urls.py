from django.urls import path
from likes import views

urlpatterns = [
    path('like/', views.LikeListView.as_view()),
    path('like/<int:pk>/', views.LikeDetailView.as_view()),
    path('love/', views.LoveListView.as_view()),
    path('love/<int:pk>/', views.LoveDetailView.as_view()),
    path('laugh/', views.LaughListView.as_view()),
    path('laugh/<int:pk>/', views.LaughDetailView.as_view()),
]