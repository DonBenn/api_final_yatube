"""Модуль содержит настройки правил запретов API."""

from rest_framework import permissions  # type: ignore


class ReadOnly(permissions.BasePermission):
    """Класс в котором предоставляется доступ.

    Если запрос безопасный до доступ предоставляется
    """

    def has_permission(self, request, view):
        """Метод проверяет безопасный ли запрос."""
        return request.method in permissions.SAFE_METHODS


class ReadForAllCreateOnlyAdmin(permissions.BasePermission):
    """Класс в котором проверяется пользователь.

    Проверяется является ли пользователь владельцем объекта,
    разрещая ему редактировать его.
    """

    def has_object_permission(self, request, view, obj):
        """Метод проверяет разрешенные методы, и является ли user автором."""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class OnlyAuthor(permissions.BasePermission):
    """Класс в котором проверяется пользователь.

    Проверяется аутефецирован ли пользователь.
    Проверяется является ли пользователь владельцем объекта,
    разрещая ему редактировать его.
    """

    def has_permission(self, request, view):
        """Метод проверяет аутефецирован ли пользователь."""
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """Метод проверяет разрешенные методы, и является ли user автором."""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class AuthorOrReadOnly(permissions.BasePermission):
    """Класс в котором проверяется пользователь.

    Проверяется аутефецирован ли пользователь.
    Проверяется является ли пользователь владельцем объекта,
    разрещая ему редактировать его.
    """

    def has_permission(self, request, view):
        """Метод проверяет аутефецирован ли пользователь.

        И безопасный ли запрос
        """
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        """Метод проверяет является ли user автором."""
        return obj.author == request.user
