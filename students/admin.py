from django.contrib import admin

from lessons.models import ScheduleItem
from teachers.models import Workload
from .models import Class


class ClassAdmin(admin.ModelAdmin):

    def sum_workload(self, obj):
        return sum([x[0] for x in Workload.objects.filter(klass=obj).values_list("workload")])

    sum_workload.short_description = "Сум. нагрузки (Занесённая)"

    def sum_workload_real(self, obj):
        return len(ScheduleItem.objects.filter(workload__klass=obj))

    sum_workload_real.short_description = "Сум. нагрузки (В рассписании)"

    def is_true(self, obj):
        return self.sum_workload(obj) == self.sum_workload_real(obj)

    is_true.boolean = True
    is_true.short_description = "Совпадение"

    def name(self, obj):
        return obj.name

    name.short_description = "Класс"

    list_display = ("id", "name", "sum_workload", "sum_workload_real", "is_true")

    list_filter = ("year", "letter_id")


admin.site.register(Class, ClassAdmin)
