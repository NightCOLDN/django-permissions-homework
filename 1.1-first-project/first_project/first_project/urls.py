from django.contrib import admin
from django.urls import path

# Импортируем наши view-функции из приложения app
from app.views import home_view, current_time_view, workdir_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1. Главная страница (пустая строка означает корень сайта / )
    path('', home_view, name='home'),

    # 2. Страница времени: current_time/
    path('current_time/', current_time_view, name='time'),

    # 3. Страница рабочей директории: workdir/
    path('workdir/', workdir_view, name='workdir'),
]
