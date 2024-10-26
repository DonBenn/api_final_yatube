"""Модуль содержит конфигурации моделей приложения Post."""
from django.contrib.auth import get_user_model  # type: ignore
from django.db import models  # type: ignore

from posts.constants import MAX_CHAR_FIELD_LENGTH, MAX_SLUG_FIELD_LENGTH

User = get_user_model()


class Group(models.Model):
    """Настройки модели Group."""

    title = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH)
    slug = models.SlugField(max_length=MAX_SLUG_FIELD_LENGTH, unique=True)
    description = models.TextField()

    class Meta:
        """Метаданные модели группы."""

        verbose_name = 'группа'
        verbose_name_plural = 'Группы'
        ordering = ('title',)

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return self.title


class Post(models.Model):
    """Настройки модели Post."""

    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        """Метаданные модели комментариев."""

        default_related_name = 'posts'
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return self.text


class Comment(models.Model):
    """Настройки модели Comment."""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        """Метаданные модели комментариев."""

        default_related_name = 'comments'
        ordering = ('created',)
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return self.text


class Follow(models.Model):
    """Настройки модели Follow."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')

    class Meta:
        """Метаданные модели подписок."""

        ordering = ('following',)
        verbose_name = 'подписчик'
        verbose_name_plural = 'Подписчики'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_user_following'
            )
        ]

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return self.user
