# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin

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

@login_required
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
            return redirect('blog:post_detail', pk=new_post.pk)
    else: # Richiesta GET
        form = PostForm()
    
    context = {
        'form': form,
        'title': 'Crea Post' # Titolo dinamico
    }
    return render(request, 'blog/post_form.html', context)
    
@login_required
def post_update_view(request, pk):
    # 1. Recupera l'oggetto o restituisci un errore 404
    #    Usiamo get_object_or_404 per gestire in modo pulito il caso in cui
    #    un post con quella 'pk' (Primary Key) non esista. È una best practice.
    post = get_object_or_404(Post, pk=pk)

    # Aggiungiamo un controllo di sicurezza: solo l'autore può modificare il post.
    if request.user != post.author:
        # Se l'utente non è l'autore, gli neghiamo l'accesso.
        # Potremmo mostrare una pagina di errore "403 Forbidden", ma per ora
        # un semplice redirect alla home è sufficiente.
        return redirect('home')

    # 2. Logica per la richiesta POST (quando l'utente invia il form)
    if request.method == 'POST':
        # La differenza chiave è qui: passiamo 'instance=post'.
        # Diciamo a Django di popolare il form con i dati inviati (request.POST)
        # ma di applicare le modifiche all'oggetto 'post' esistente.
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            # Reindirizziamo alla pagina di dettaglio del post appena modificato.
            return redirect('blog:post_detail', pk=post.pk)
    # 3. Logica per la richiesta GET (quando l'utente visita la pagina)
    else:
        # Anche qui passiamo 'instance=post'.
        # Questo dice a Django di creare un form pre-compilato
        # con i dati attuali dell'oggetto 'post'.
        form = PostForm(instance=post)

    # 4. Render del template
    #    Passiamo il form e l'oggetto post al template.
    #    Aggiungiamo un titolo per rendere il template riutilizzabile.
    context = {
        'form': form,
        'post': post,
        'title': 'Modifica Post' # Titolo dinamico
    }
    return render(request, 'blog/post_form.html', context)



from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')

    def test_func(self):
        """Questo test viene eseguito da UserPassesTestMixin."""
        post = self.get_object() # Recupera l'oggetto post che si sta cercando di cancellare
        return self.request.user == post.author # Restituisce True solo se l'utente è l'autore

