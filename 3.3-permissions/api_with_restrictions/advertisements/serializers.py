from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    # Делаем поле creator обычным read_only (подставлять его будем во ViewSet)
    creator = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'description', 'status', 'creator', 'created_at']

    def validate(self, data):
        """Метод для валидации данных при создании и обновлении объявления."""
        status = data.get('status', 'OPEN')
        user = self.context['request'].user

        if self.context['request'].method == 'POST' or status == 'OPEN':
            open_ads_count = Advertisement.objects.filter(creator=user, status='OPEN').count()

            if open_ads_count >= 10:
                if self.instance and self.instance.status == 'OPEN':
                    return data
                raise ValidationError("У вас не может быть более 10 открытых объявлений одновременно.")

        return data

