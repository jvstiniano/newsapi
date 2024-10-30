from rest_framework import permissions
from django.contrib.auth import get_user_model

User = get_user_model()

class IsEditor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.Role.EDITOR

class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.Role.USER