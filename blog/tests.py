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
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.post = Post.objects.create(
            title='Un Titolo di Test',
            content='Contenuto del post di test.',
            author=self.user
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')
        self.assertContains(response, self.post.title) # Controlla che il titolo sia nell'HTML

    def test_post_detail_view(self):
        response = self.client.get(reverse('blog:post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.content)

    def test_post_create_view_redirects_if_not_logged_in(self):
        response = self.client.get(reverse('blog:post_create'))
        # Un utente non loggato viene reindirizzato
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/post/new/')

    def test_post_create_view_if_logged_in(self):
        # Logghiamo l'utente
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('blog:post_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')