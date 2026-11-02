from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Подключаем все маршруты из приложения stations в корень нашего сайта
    path('', include('stations.urls')),
]
