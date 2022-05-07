from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrIsAuthenticated(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
            bool(request.user and request.user.is_authenticated) 
            if request.method in SAFE_METHODS else obj.author == request.user
        )
