import os  # Нужен для работы с файлами (listdir)
from datetime import datetime  # Нужен для получения времени
from django.http import HttpResponse
from django.shortcuts import render, reverse

def home_view(request):
    template_name = 'app/home.html'

    # Здесь мы формируем список страниц для шаблона, который вам дали в заготовке.
    # Функция reverse автоматически находит URL-адрес по имени маршрута (name из urls.py)
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # Контекст — это данные, которые передаются внутрь HTML-шаблона
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def current_time_view(request):
    # 1. Получаем текущее время
    now = datetime.now()
    # 2. Форматируем его в красивую строчку (Часы:Минуты:Секунды)
    msg = f"Текущее время: {now.strftime('%H:%M:%S')}"
    # 3. Возвращаем обычный текстовый ответ на страницу
    return HttpResponse(msg)


def workdir_view(request):
    # 1. Получаем список файлов в текущей рабочей директории проекта
    files_list = os.listdir('.')

    # 2. Красиво объединяем список файлов через тег <br/> (перенос строки в HTML),
    # чтобы файлы вывелись аккуратным списком друг под другом, а не в одну строчку
    msg = f"Содержимое рабочей директории:<br/>" + "<br/>".join(files_list)

    # 3. Возвращаем результат
    return HttpResponse(msg)
