# blog/views.py
from django.shortcuts import get_object_or_404, render
from .models import Post # Importiamo il modello Post

def post_list_view(request):
    posts = Post.objects.select_related('author').all().order_by('-created_at') # Prendiamo tutti i post, i più recenti prima
    context = {
        'posts': posts,
    }
    return render(request, "blog/post_list.html", context)

def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    return render(request, "blog/post_detail.html", context)