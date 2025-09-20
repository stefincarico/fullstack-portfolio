from rest_framework.response import Response
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404
from blog.models import Post, Tag
from .serializers import PostSerializer, TagSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from .permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly] 

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class TagViewSet(viewsets.ModelViewSet):
    """
    Un ViewSet per visualizzare e modificare i tag.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer