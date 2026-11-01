from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """Право доступа: изменять объект может только автор, остальные — только смотреть."""

    def has_object_permission(self, request, view, obj):
        # Если метод запроса безопасный (GET, HEAD, OPTIONS) — разрешаем всем
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Если это изменение или удаление, проверяем, является ли пользователь автором
        return request.user == obj.creator
