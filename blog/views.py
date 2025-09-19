# blog/views.py
from django.shortcuts import render
from .models import Post # Importiamo il modello Post

def post_list_view(request):
    posts = Post.objects.all().order_by('-created_at') # Prendiamo tutti i post, i più recenti prima
    context = {
        'posts': posts,
    }
    return render(request, "blog/post_list.html", context)