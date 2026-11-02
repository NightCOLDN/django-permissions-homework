from django.shortcuts import render
from .models import Student

def students_list(request):
    template = 'school/students_list.html'

    # prefetch_related достанет учителей за 1 дополнительный запрос (оптимизация по ТЗ)
    ordering = 'group'
    object_list = Student.objects.all().prefetch_related('teachers').order_by(ordering)

    context = {
        'object_list': object_list
    }

    return render(request, template, context)
