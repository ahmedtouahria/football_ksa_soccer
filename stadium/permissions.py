from rest_framework import permissions
from rest_framework.response import Response

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
"""Custom permission for stadium owner or read only"""
class IsStadiumOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner.user==request.user
class IsStadiumOwnerOrReadOnlyForOrders(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method not in ('PUT','DELETE','POST'):
            return True
        return obj.stadium.owner.user==request.user
