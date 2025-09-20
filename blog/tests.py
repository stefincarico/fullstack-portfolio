# blog/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):

    def setUp(self):
        """
        Il metodo setUp viene eseguito PRIMA di ogni test. 
        È utile per creare oggetti che useremo in più test.
        """
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.post = Post.objects.create(
            title='Un Titolo di Test',
            content='Contenuto del post di test.',
            author=self.user
        )

    def test_string_representation(self):
        self.assertEqual(str(self.post), self.post.title)

class PostViewTest(TestCase):

    def setUp(self):
        User = get_user_model()
        # Utente 1 (il nostro utente principale per i test)
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.post = Post.objects.create(
            title='Un Titolo di Test',
            content='Contenuto del post di test.',
            author=self.user
        )
        # Utente 2 (per i test di autorizzazione)
        self.other_user = User.objects.create_user(username='otheruser', password='password123')
        self.other_post = Post.objects.create(
            title='Un Altro Titolo',
            content='Contenuto di un altro utente.',
            author=self.other_user
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')
        self.assertContains(response, self.post.title)

    def test_post_detail_view(self):
        response = self.client.get(reverse('blog:post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.content)

    def test_post_create_view_redirects_if_not_logged_in(self):
        response = self.client.get(reverse('blog:post_create'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/post/create/')

    def test_post_create_view_if_logged_in(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('blog:post_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')

    # --- NUOVI TEST PER UPDATE VIEW ---

    def test_post_update_view_redirects_if_not_logged_in(self):
        """Verifica che un utente anonimo venga reindirizzato se tenta di modificare un post."""
        response = self.client.get(reverse('blog:post_update', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next=/post/{self.post.pk}/edit/')

    def test_post_update_view_for_author(self):
        """Verifica che l'autore di un post possa accedere alla pagina di modifica."""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('blog:post_update', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')

    def test_post_update_view_redirects_for_other_user(self):
        """Verifica che un utente venga reindirizzato se tenta di modificare il post di un altro."""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('blog:post_update', args=[self.other_post.pk]))
        # La nostra view reindirizza alla home (302), non dà un 403. Testiamo questo comportamento.
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    # --- NUOVI TEST PER DELETE VIEW ---

    def test_post_delete_view_redirects_if_not_logged_in(self):
        """Verifica che un utente anonimo venga reindirizzato se tenta di cancellare un post."""
        response = self.client.get(reverse('blog:post_delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next=/post/{self.post.pk}/delete/')

    def test_post_delete_view_for_author(self):
        """Verifica che l'autore possa accedere alla pagina di conferma cancellazione."""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('blog:post_delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_confirm_delete.html')

    def test_post_delete_view_forbidden_for_other_user(self):
        """Verifica che un utente NON possa accedere alla pagina di cancellazione di altri."""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('blog:post_delete', args=[self.other_post.pk]))
        # Ci aspettiamo un errore 403 Forbidden, perché l'utente non ha i permessi.
        self.assertEqual(response.status_code, 403)