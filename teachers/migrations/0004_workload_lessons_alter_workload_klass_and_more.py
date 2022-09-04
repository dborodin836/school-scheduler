# Generated by Django 4.1 on 2022-09-03 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_class_options_alter_class_letter_id_and_more'),
        ('lessons', '0003_remove_lesson_teacher'),
        ('teachers', '0003_remove_teacher_workload_workload'),
    ]

    operations = [
        migrations.AddField(
            model_name='workload',
            name='lessons',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson', verbose_name='Предмет'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workload',
            name='klass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.class', verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='workload',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher', verbose_name='Учитель'),
        ),
        migrations.AlterField(
            model_name='workload',
            name='workload',
            field=models.PositiveSmallIntegerField(verbose_name='Нагрузка'),
        ),
    ]