from rest_framework import permissions
from rest_framework.response import Response

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
"""Custom permission for stadium owner or read only"""
class IsClubeCapitanOrReadOnly(permissions.BasePermission):
    """custom permission for is clube capitan or read only """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.capitan.user==request.user

class IsCapitanOrReadOnlyClubeMembers(permissions.BasePermission):
    """custom permission for is clube capitan or read only """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.clube.capitan.user==request.user