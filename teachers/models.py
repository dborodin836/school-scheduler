import datetime

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
        result = sorted(list(result))
        if not result:
            return None
        return result

    def is_available_lesson(self, date: datetime.datetime, lesson_no: int) -> bool:
        available_lessons = self.get_available_lessons(date)

        if available_lessons is None:
            return False

        if lesson_no in available_lessons:
            return True

    def __str__(self):
        return self.name


class Workload(models.Model):

    CHOICES = (
        (0.5, "0.5"),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13'),
        (14, '14'),
        (15, '15'),
        (16, '16'),
        (17, '17'),
        (18, '18'),
        (19, '19'),
        (20, '20'),
        (21, '21'),
        (22, '22'),
        (23, '23'),
        (24, '24'),
        (25, '25'),
        (26, '26'),
        (27, '27'),
        (28, '28'),
        (29, '29'),
        (30, '30'),
        (31, '31'),
        (32, '32'),
        (33, '33'),
        (34, '34'),
    )

    klass = models.ForeignKey("students.Class", on_delete=models.CASCADE, verbose_name="Класс")
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE, verbose_name="Учитель")
    workload = models.DecimalField(decimal_places=1, max_digits=3, choices=CHOICES, verbose_name="Нагрузка", default=0)
    lessons = models.ForeignKey("lessons.Lesson", on_delete=models.CASCADE, verbose_name="Предмет")

    class Meta:
        verbose_name = "Нагрузка"
        verbose_name_plural = "Нагрузка учителей"
        unique_together = [["klass", "teacher", "lessons"]]

    def __str__(self):
        return f"{self.teacher.name} - {self.klass.get_name()} ({self.workload} часов {self.lessons})"
