# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from blog.models import Post
from .serializers import PostSerializer

class PostListApiView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        Restituisce la lista di tutti i post.
        '''
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PostDetailApiView(APIView):
    def get(self, request, pk, *args, **kwargs):
        '''
        Restituisce i dettagli di un singolo post.
        '''
        # 1. Recupera il singolo oggetto usando la pk e get_object_or_404
        post = get_object_or_404(Post, pk=pk)
        # 2. Serializza il singolo oggetto (NON serve many=True)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)