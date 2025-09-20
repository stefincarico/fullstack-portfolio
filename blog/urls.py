# blog/urls.py
from django.urls import path
from .views import post_list_view, post_detail_view, post_create_view, post_update_view

app_name = 'blog'

urlpatterns = [
    path('', post_list_view, name='post_list'),
    path('post/create/', post_create_view, name='post_create'),
    path('post/<int:pk>/', post_detail_view, name='post_detail'),
    path('post/<int:pk>/edit/', post_update_view, name='post_update'),
]