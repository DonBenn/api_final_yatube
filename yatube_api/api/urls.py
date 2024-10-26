"""Модуль содержит URL настройки адрессов приложения API."""
from django.urls import include, path  # type: ignore
from rest_framework.routers import DefaultRouter  # type: ignore

from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='post')
router_v1.register(r'groups', GroupViewSet, basename='group')
router_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='commentlist'
                   )
router_v1.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
