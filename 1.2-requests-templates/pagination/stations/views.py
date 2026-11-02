import csv
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

def index(request):
    # Эта функция срабатывает на главной странице и автоматически
    # перенаправляет (делает редирект) пользователя на адрес со списком остановок
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # 1. Создаем пустой список, куда будем складывать остановки
    stations = []

    # 2. Открываем CSV-файл с остановками Москвы
    # Путь к нему уже прописан в настройках Нетологии в переменной settings.BUS_STATION_CSV
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Из каждой строчки CSV берем три колонки и добавляем в наш список
            stations.append({
                'Name': row['Name'],
                'Street': row['Street'],
                'District': row['District']
            })

    # 3. Считываем номер текущей страницы из строки браузера (например, ?page=2)
    # Если параметра нет, по умолчанию открываем 1-ю страницу
    current_page = request.GET.get('page', 1)

    # 4. Инициализируем пагинатор Django: разбиваем список остановок по 10 штук на страницу
    paginator = Paginator(stations, 10)

    # 5. Получаем объект конкретной текущей страницы
    page = paginator.get_page(current_page)

    # 6. Передаем данные в контекст шаблона (именно эти имена переменных ожидает шаблон Нетологии)
    context = {
        'bus_stations': page.object_list,  # Список из 10 остановок для отображения в таблице
        'page': page,                      # Объект страницы для работы кнопок «Вперед/Назад»
    }

    # Возвращаем готовый шаблон
    return render(request, 'stations/index.html', context)
