from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tags_count = 0
        has_tags = False

        for form in self.forms:
            # Проверяем только те формы, которые не отмечены на удаление
            if form.cleaned_data and not form.cleaned_data.get('DELETE'):
                has_tags = True
                if form.cleaned_data.get('is_main'):
                    main_tags_count += 1

        # Если у статьи есть хотя бы один тег, проверяем правила
        if has_tags:
            if main_tags_count == 0:
                raise ValidationError('Укажите основной раздел для статьи.')
            if main_tags_count > 1:
                raise ValidationError('Основным разделом может быть только один.')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
