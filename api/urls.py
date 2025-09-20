# api/urls.py
from django.urls import path
from .views import PostListApiView, PostDetailApiView

urlpatterns = [
    path('posts/', PostListApiView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailApiView.as_view(), name='post-detail'),
]