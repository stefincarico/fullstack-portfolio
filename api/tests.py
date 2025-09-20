# api/tests.py
import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from blog.models import Post

# Questo marcatore dice a pytest che tutti i test in questo file 
# hanno bisogno di accedere al database.
@pytest.mark.django_db
class TestPostViewSet:

    def setup_method(self):
        """
        Metodo di setup eseguito prima di ogni test nella classe.
        Simile a setUp in unittest.
        """
        self.client = APIClient()
        User = get_user_model()
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')

        self.post1 = Post.objects.create(
            title='Post di User 1',
            content='Contenuto...',
            author=self.user1
        )

    def test_list_posts_unauthenticated(self):
        response = self.client.get('/api/v1/posts/')
        assert response.status_code == 200
        assert len(response.data) > 0 # Ci aspettiamo che la lista non sia vuota

    def test_create_post_unauthenticated(self):
        response = self.client.post('/api/v1/posts/', {'title': 'Nuovo Titolo', 'content': '...'})
        assert response.status_code == 403 # Forbidden

    def test_create_post_authenticated(self):
        # Autentichiamo il client per questa richiesta
        self.client.force_authenticate(user=self.user1)
        
        data = {'title': 'Titolo Autenticato', 'content': 'Contenuto creato da user1'}
        response = self.client.post('/api/v1/posts/', data)
        
        assert response.status_code == 201 # Created
        assert response.data['title'] == 'Titolo Autenticato'
        assert response.data['author_username'] == self.user1.username
        assert Post.objects.count() == 2 # Ora dovremmo avere 2 post nel DB di test

    def test_update_own_post(self):
        self.client.force_authenticate(user=self.user1)
        
        data = {'title': 'Titolo Modificato'}
        # Usiamo PATCH per un aggiornamento parziale
        response = self.client.patch(f'/api/v1/posts/{self.post1.pk}/', data)
        
        assert response.status_code == 200
        assert response.data['title'] == 'Titolo Modificato'
        # Ricarichiamo l'oggetto dal DB per essere sicuri che la modifica sia avvenuta
        self.post1.refresh_from_db()
        assert self.post1.title == 'Titolo Modificato'

    def test_update_other_user_post_fails(self):
        # Ci autentichiamo come user2
        self.client.force_authenticate(user=self.user2)
        
        data = {'title': 'Titolo Hackerato'}
        # E proviamo a modificare il post di user1
        response = self.client.patch(f'/api/v1/posts/{self.post1.pk}/', data)
        
        assert response.status_code == 403 # Forbidden!

    def test_delete_other_user_post_fails(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.delete(f'/api/v1/posts/{self.post1.pk}/')
        assert response.status_code == 403 # Forbidden!
        assert Post.objects.count() == 1 # Il post non deve essere stato cancellato

    def test_search_posts(self):
        """
        Verifica che la ricerca per titolo e contenuto funzioni correttamente.
        """
        # Arrange: Crea post specifici per il test di ricerca.
        # Il post 'Post di User 1' esiste già dal setup.
        Post.objects.create(title='Un titolo che parla di Python', content='...', author=self.user1)
        Post.objects.create(title='Un titolo su Django', content='...', author=self.user1)
        
        # Act: Esegui la ricerca per la parola "Python"
        response = self.client.get('/api/v1/posts/?search=Python')
        
        # Assert
        assert response.status_code == 200
        # Ci sono 3 post in totale nel DB, ma solo 1 deve corrispondere alla ricerca
        assert len(response.data) == 1
        assert response.data[0]['title'] == 'Un titolo che parla di Python'


