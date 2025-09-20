from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from blog.models import Post, Tag
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, TagSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly] 
    filterset_fields = ['author', 'tags']
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class TagViewSet(viewsets.ModelViewSet):
    """
    Un ViewSet per visualizzare e modificare i tag.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    search_fields = ['name']

