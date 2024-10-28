"""Модуль содержит настройки сериализаторов приложения API."""
from rest_framework import serializers   # type: ignore
from rest_framework.validators import UniqueTogetherValidator  # type: ignore

from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    """Настройки сериализатора модели Post."""

    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        """Метаданные сериализатора постов."""

        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Настройки сериализатора модели Comment."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        """Метаданные сериализатора комментариев."""

        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    """Настройки сериализатора модели Group."""

    class Meta:
        """Метаданные сериализатора группы."""

        model = Group
        fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    """Настройки сериализатора модели Follow."""

    user = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field='username', queryset=User.objects.all()
    )
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )

    class Meta:
        """Метаданные сериализатора подписчиков."""

        model = Follow
        fields = ('following', 'user')
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

    def validate_following(self, value):
        """Метод валидации отдельного поля сериализатора."""
        if self.context['request'].user == value:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя.'
            )
        return value
