from django.db import models

from core.models import TimeStampedAddedByModel
from teachers.models import Teacher


class Lesson(TimeStampedAddedByModel):

    title = models.CharField(max_length=64, verbose_name="Урок")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.title
