from django.shortcuts import render

# База данных рецептов от Нетологии
DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
        'томаты, г': 0.2,
    },
    'buter': {
        'хлеб, кусок': 1,
        'колбаса, кусок': 1,
        'сыр, кусок': 1,
        'помидор, кусок': 1,
    },
    # можете добавить свои рецепты по желанию
}

def recipe_view(request, dish_name):
    # 1. Проверяем, есть ли такое блюдо в нашей базе данных
    dish = DATA.get(dish_name)

    if dish:
        # 2. Получаем параметр количества порций из URL-строки (например, ?servings=3)
        # По умолчанию, если параметр не указан, берем 1 порцию.
        servings = request.GET.get('servings', 1)

        try:
            # Превращаем в целое число, на случай если пользователь ввёл строку
            servings = int(servings)
        except ValueError:
            # Если ввели ерунду (например, ?servings=abc), сбрасываем на 1 порцию
            servings = 1

        # 3. Пересчитываем ингредиенты: умножаем исходное количество на количество порций
        recipe = {}
        for ingredient, amount in dish.items():
            recipe[ingredient] = amount * servings

        context = {
            'recipe': recipe
        }
    else:
        # Если блюдо не найдено, передаем пустой контекст (шаблон сам покажет, что рецепта нет)
        context = {
            'recipe': None
        }

    # Возвращаем готовый HTML-шаблон index.html (он уже лежит в папке templates задачи)
    return render(request, 'calculator/index.html', context)
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
        'томаты, г': 0.2,
    },
    'buter': {
        'хлеб, кусок': 1,
        'колбаса, кусок': 1,
        'сыр, кусок': 1,
        'помидор, кусок': 1,
    },
}

# НОВАЯ ФУНКЦИЯ ДЛЯ ГЛАВНОЙ СТРАНИЦЫ
def home_view(request):
    # Из словаря DATA получаем список всех доступных ключей-блюд: ['omlet', 'pasta', 'buter']
    dishes = list(DATA.keys())
    context = {
        'dishes': dishes
    }
    # Используем тот же шаблон index.html
    return render(request, 'calculator/index.html', context)

# Существующую функцию recipe_view оставляем без изменений
def recipe_view(request, dish_name):
    dish = DATA.get(dish_name)
    if dish:
        servings = request.GET.get('servings', 1)
        try:
            servings = int(servings)
        except ValueError:
            servings = 1

        recipe = {}
        for ingredient, amount in dish.items():
            recipe[ingredient] = amount * servings

        context = {
            'recipe': recipe,
            'dish_name': dish_name  # Добавим имя блюда для красоты в шаблоне
        }
    else:
        context = {
            'recipe': None
        }
    return render(request, 'calculator/index.html', context)
