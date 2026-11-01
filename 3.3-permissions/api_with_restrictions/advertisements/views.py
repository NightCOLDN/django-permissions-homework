from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.filters import AdvertisementFilter
from advertisements.permissions import IsOwnerOrReadOnly


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticatedOrReadOnly(), IsOwnerOrReadOnly()]
        return []

    def perform_create(self, serializer):
        """Автоматически подставляем текущего пользователя как создателя объявления."""
        # Метод save() принимает дополнительные параметры и передаёт их напрямую в БД
        serializer.save(creator=self.request.user)
