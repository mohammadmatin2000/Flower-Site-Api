from rest_framework import permissions
# ======================================================================================================================
class IsAdminOrSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and user.type in [2, 3])  # 2=admin, 3=superuser
# ======================================================================================================================