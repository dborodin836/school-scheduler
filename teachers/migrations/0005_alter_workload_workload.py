# Generated by Django 4.1 on 2022-09-03 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_workload_lessons_alter_workload_klass_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workload',
            name='workload',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Нагрузка'),
        ),
    ]