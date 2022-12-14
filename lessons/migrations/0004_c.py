# Generated by Django 4.1 on 2022-09-03 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0005_alter_workload_workload'),
        ('lessons', '0003_remove_lesson_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='c',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_no', models.CharField(choices=[('1', '1 урок'), ('2', '2 урок'), ('3', '3 урок'), ('4', '4 урок'), ('5', '5 урок'), ('6', '6 урок'), ('7', '7 урок')], max_length=15)),
                ('workload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.workload')),
            ],
        ),
    ]
