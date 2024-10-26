"""Модуль содержит настройки view-функций приложения API."""

from django.shortcuts import get_object_or_404  # type: ignore
from rest_framework import viewsets, filters   # type: ignore
from rest_framework.pagination import LimitOffsetPagination   # type: ignore

from api.permissions import (
    ReadForAllCreateOnlyAdmin, OnlyAuthor, ReadOnly, AuthorOrReadOnly
)
from api.serializers import (
    PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer,
)
from posts.models import Post, Group, Follow


class PostViewSet(viewsets.ModelViewSet):
    """Настройки вьюсета модели Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AuthorOrReadOnly]
    pagination_class = LimitOffsetPagination
    ordering_fields = ('-pub_date',)

    def get_permissions(self):
        """Определяет необходимый набор ограничений."""
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    def perform_create(self, serializer):
        """Создание нового экземпляра модели после сериализации."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Настройки вьюсета модели Group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [ReadForAllCreateOnlyAdmin]
    ordering_fields = ('title',)


class CommentViewSet(viewsets.ModelViewSet):
    """Настройки view класса модели Comment."""

    serializer_class = CommentSerializer
    permission_classes = [AuthorOrReadOnly]
    ordering_fields = ('created',)

    def get_permissions(self):
        """Определяет необходимый набор ограничений."""
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    def get_queryset(self):
        """Определяет необходимый набор queryset для сериализации."""
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        """Создание нового экземпляра модели после сериализации."""
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    """Настройки view класса модели Follow."""

    permission_classes = [OnlyAuthor]
    filter_backends = (filters.SearchFilter,)
    serializer_class = FollowSerializer
    search_fields = ('following__username',)
    ordering_fields = ('following',)

    def get_queryset(self):
        """Определяет необходимый набор queryset для сериализации."""
        user = self.request.user
        new_queryset = Follow.objects.filter(user=user)
        return new_queryset

    def perform_create(self, serializer):
        """Создание нового экземпляра модели после сериализации."""
        serializer.save(user=self.request.user)
