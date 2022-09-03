from django.db import models

from core.models import TimeStampedAddedByModel
# from lessons.models import Lesson
from students.models import Class


class Teacher(TimeStampedAddedByModel):

    name = models.CharField(max_length=128, verbose_name="Имя")
    # curating_class = models.OneToOneField(verbose_name="Классный руководитель", blank=True)

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"

    def __str__(self):
        return self.name


class Workload(models.Model):

    klass = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name="Класс")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Учитель")
    workload = models.PositiveSmallIntegerField(verbose_name="Нагрузка", default=0)
    lessons = models.ForeignKey("lessons.Lesson", on_delete=models.CASCADE, verbose_name="Предмет")

    class Meta:
        verbose_name = "Нагрузка"
        verbose_name_plural = "Нагрузка учителей"

    def __str__(self):
        return f"{self.teacher.name} - {self.klass.get_name()} ({self.workload} часов)"
