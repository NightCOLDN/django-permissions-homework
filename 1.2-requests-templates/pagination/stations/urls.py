from django.urls import path
from stations.views import index, bus_stations

urlpatterns = [
    # Главная страница приложения (делает редирект)
    path('', index, name='index'),

    # Страница со списком автобусных остановок: /bus_stations/
    path('bus_stations/', bus_stations, name='bus_stations'),
]
