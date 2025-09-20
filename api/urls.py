# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, TagViewSet

# Creiamo un router e registriamo i nostri ViewSet
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post') # Registriamo il PostViewSet
router.register(r'tags', TagViewSet, basename='tag')

# Gli URL dell'API sono una combinazione di quelli manuali e quelli generati dal router
urlpatterns = [
    path('', include(router.urls)), # Includiamo gli URL generati dal router
]