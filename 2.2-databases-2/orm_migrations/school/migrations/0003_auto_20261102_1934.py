from django.db import migrations

def forward_func(apps, schema_editor):
    # Получаем живые модели из текущего состояния миграций
    Student = apps.get_model('school', 'Student')

    # Проходимся циклом по каждому ученику в базе данных
    for student in Student.objects.all():
        # Если у ученика заполнен старый учитель
        if student.teacher:
            # Добавляем этого учителя в наше новое поле ManyToMany
            student.teachers.add(student.teacher)

def backward_func(apps, schema_editor):
    # Логика отката миграции (если потребуется вернуть всё назад)
    Student = apps.get_model('school', 'Student')
    for student in Student.objects.all():
        first_teacher = student.teachers.first()
        if first_teacher:
            student.teacher = first_teacher
            student.save()

class Migration(migrations.Migration):

    dependencies = [
        # Убедитесь, что имя предыдущей миграции совпадает с вашей (0002_...)
        ('school', '0002_student_teachers_alter_student_group_and_more'),
    ]

    operations = [
        migrations.RunPython(forward_func, backward_func),
    ]
