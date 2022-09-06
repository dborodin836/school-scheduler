from django.db import models

from core.models import TimeStampedAddedByModel


class Lesson(TimeStampedAddedByModel):

    title = models.CharField(max_length=64, verbose_name="Урок")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.title


class ScheduleItem(models.Model):
    CHOICES = [
        ('1', '1 урок'),
        ('2', '2 урок'),
        ('3', '3 урок'),
        ('4', '4 урок'),
        ('5', '5 урок'),
        ('6', '6 урок'),
        ('7', '7 урок')
    ]
    lesson_no = models.CharField(choices=CHOICES, max_length=15)
    workload = models.ForeignKey("teachers.Workload", on_delete=models.CASCADE)
    date = models.DateField(verbose_name="Дата", default="2022-1-1")

    def __str__(self):
        return f"{self.workload.lessons} | {self.workload.teacher}"

    class Meta:
        verbose_name = "Ячейка рассписания"
        verbose_name_plural = "Ячейки рассписания"
