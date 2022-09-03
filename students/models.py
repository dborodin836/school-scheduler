from django.db import models

from core.models import TimeStampedAddedByModel


class Class(TimeStampedAddedByModel):

    year = models.PositiveSmallIntegerField(verbose_name="Год обучения")
    letter_id = models.CharField(max_length=2, verbose_name="Буквенное обозначение")

    class Meta:
        verbose_name = "Класс"
        verbose_name_plural = "Классы"

    def get_name(self):
        return f"{self.year}-{self.letter_id}"

    def __str__(self):
        return self.get_name()