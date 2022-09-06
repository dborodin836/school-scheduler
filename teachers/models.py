from django.db import models

from core.models import TimeStampedAddedByModel
from lessons.models import ScheduleItem


class Teacher(TimeStampedAddedByModel):

    name = models.CharField(max_length=128, verbose_name="Имя")
    # curating_class = models.OneToOneField(verbose_name="Классный руководитель", blank=True)

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"

    def get_available_lessons(self, date):
        available_lesson = {1, 2, 3, 4, 5, 6, 7}
        query = ScheduleItem.objects.filter(workload__teacher=self, date=date).values_list("lesson_no")
        query = set(map(lambda x: int(x[0]), query))
        result = available_lesson.difference(set(query))
        if not result:
            return None
        return result

    def __str__(self):
        return self.name


class Workload(models.Model):

    klass = models.ForeignKey("students.Class", on_delete=models.CASCADE, verbose_name="Класс")
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE, verbose_name="Учитель")
    workload = models.PositiveSmallIntegerField(verbose_name="Нагрузка", default=0)
    lessons = models.ForeignKey("lessons.Lesson", on_delete=models.CASCADE, verbose_name="Предмет")

    class Meta:
        verbose_name = "Нагрузка"
        verbose_name_plural = "Нагрузка учителей"

    def __str__(self):
        return f"{self.teacher.name} - {self.klass.get_name()} ({self.workload} часов {self.lessons})"
