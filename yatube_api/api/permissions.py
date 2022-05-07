from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrIsAuthenticated(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            if request.method not in SAFE_METHODS
            else bool(request.user and request.user.is_authenticated)
        )
