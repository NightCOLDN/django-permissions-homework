from django.shortcuts import render
from articles.models import Article

def articles_list(request):
    template = 'articles/news.html'

    # 1. Оптимизировано загружаем статьи вместе со связанными объектами Scope и тегами Tag
    # Используем двойное подчёркивание для сквозной предзагрузки: scopes__tag
    articles = Article.objects.all().prefetch_related('scopes__tag').order_by('-published_at')

    # 2. Передаем готовый список статей в контекст шаблона
    context = {
        'object_list': articles
    }

    return render(request, template, context)
