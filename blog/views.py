# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required 

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

def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Salviamo il form, ma non ancora nel DB
            new_post = form.save(commit=False)
            # Assegniamo l'autore (l'utente attualmente loggato)
            new_post.author = request.user 
            new_post.save()
            # I ManyToMany si salvano solo dopo che l'oggetto principale esiste
            form.save_m2m() 
            return redirect('post_detail', pk=new_post.pk)
    else: # Richiesta GET
        form = PostForm()
    
    context = {
        'form': form,
    }
    return render(request, 'blog/post_form.html', context)
    
    