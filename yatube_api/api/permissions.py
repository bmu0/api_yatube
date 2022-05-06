from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrIsAuthenticated(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        return obj.author == request.user
