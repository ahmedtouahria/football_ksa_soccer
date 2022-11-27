from rest_framework import permissions
from rest_framework.response import Response

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsArbitre(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user.arbitre and
            request.user.is_authenticated
        )

