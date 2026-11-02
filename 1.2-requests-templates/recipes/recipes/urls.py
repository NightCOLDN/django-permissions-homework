from django.contrib import admin
from django.urls import path
from calculator.views import recipe_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1. При переходе на самый корень сайта (http://127.0.0) откроется меню
    path('', home_view, name='home'),

    # 2. При переходе на /calculator/ тоже откроется меню
    path('calculator/', home_view, name='calculator_home'),

    # 3. При переходе на конкретное блюдо (http://127.0.0omlet/ или /calculator/omlet/)
    path('<str:dish_name>/', recipe_view, name='recipe'),
    path('calculator/<str:dish_name>/', recipe_view, name='recipe_alt'),
]
