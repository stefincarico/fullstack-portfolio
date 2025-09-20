# api/permissions.py
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Permesso personalizzato per consentire solo agli autori di un oggetto di modificarlo.
    """
    def has_object_permission(self, request, view, obj):
        # Le richieste di lettura (GET, HEAD, OPTIONS) sono sempre permesse.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Le autorizzazioni di scrittura sono permesse solo se l'utente è l'autore del post.
        return obj.author == request.user