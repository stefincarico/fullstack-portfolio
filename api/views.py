# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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