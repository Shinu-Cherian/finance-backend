from rest_framework.permissions import BasePermission, SAFE_METHODS

class RoleBasedPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user

        # If user not logged in
        if not user.is_authenticated:
            return False

        # Viewer → only GET (read)
        if user.role == 'viewer':
            return request.method in SAFE_METHODS

        # Analyst → also only read (for now)
        if user.role == 'analyst':
            return request.method in SAFE_METHODS

        # Admin → full access
        if user.role == 'admin':
            return True

        return False