from django.contrib import admin

from lessons.models import ScheduleItem
from teachers.models import Workload
from .models import Class


class ClassAdmin(admin.ModelAdmin):

    def sum_workload(self, obj):
        return sum([x[0] for x in Workload.objects.filter(klass=obj).values_list("workload")])

    sum_workload.short_description = "Сумма нагрузки (Занесённая)"

    def sum_workload_real(self, obj):
        return len(ScheduleItem.objects.filter(workload__klass=obj))

    sum_workload_real.short_description = "Сумма нагрузки (В рассписании)"

    list_display = ("id", "year", "letter_id", "sum_workload", "sum_workload_real")


admin.site.register(Class, ClassAdmin)
