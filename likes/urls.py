from django.urls import path
from likes import views

urlpatterns = [
    path('likes/', views.LikeList.as_view()),
    path('likes/<int:pk>/', views.LikeDetail.as_view()),
    path('loves/', views.LoveList.as_view()),
    path('loves/<int:pk>/', views.LoveDetail.as_view()),
    path('laughs/', views.LaughList.as_view()),
    path('laughs/<int:pk>/', views.LaughDetail.as_view()),
]