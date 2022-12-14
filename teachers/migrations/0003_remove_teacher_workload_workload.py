# Generated by Django 4.1 on 2022-09-03 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_class_options_alter_class_letter_id_and_more'),
        ('teachers', '0002_alter_teacher_options_alter_teacher_workload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='workload',
        ),
        migrations.CreateModel(
            name='Workload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workload', models.PositiveSmallIntegerField()),
                ('klass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.class')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher')),
            ],
            options={
                'verbose_name': 'Нагрузка',
                'verbose_name_plural': 'Нагрузка учителей',
            },
        ),
    ]
