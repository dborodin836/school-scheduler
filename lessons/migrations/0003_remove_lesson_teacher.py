# Generated by Django 4.1 on 2022-09-03 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_alter_lesson_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='teacher',
        ),
    ]