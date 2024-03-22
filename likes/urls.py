from django.urls import path
from likes import views

urlpatterns = [
    path('likes/', views.LikeListView.as_view()),
    path('likes/<int:pk>/', views.LikeDetailView.as_view()),
    path('loves/', views.LoveListView.as_view()),
    path('loves/<int:pk>/', views.LoveDetailView.as_view()),
    path('laughs/', views.LaughListView.as_view()),
    path('laughs/<int:pk>/', views.LaughDetailView.as_view()),
]