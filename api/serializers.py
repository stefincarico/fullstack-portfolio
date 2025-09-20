# api/serializers.py
from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    # Aggiungiamo un campo extra per mostrare l'username dell'autore
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author_username', 'created_at')