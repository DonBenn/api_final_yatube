"""Модуль содержит конфигурации приложения API."""
from django.apps import AppConfig  # type: ignore


class ApiConfig(AppConfig):
    """Конфигурация приложения API."""

    name = 'api'
