from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # Добавляем фильтр диапазона дат для поля created_at
    # Он позволит делать запросы вида: ?created_at_before=2026-11-01&created_at_after=2026-10-01
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        # Указываем, какие поля из базы данных будут участвовать в фильтрации
        # Поле 'status' сгенерирует фильтр автоматически по точному совпадению (OPEN/CLOSED)
        fields = ['created_at', 'status']
