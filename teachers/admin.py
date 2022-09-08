import datetime

from django.contrib import admin

from lessons.models import ScheduleItem
from .models import Teacher, Workload


class TeacherAdmin(admin.ModelAdmin):

    def sum_workload(self, obj):
        return sum([x[0] for x in Workload.objects.filter(teacher=obj).values_list("workload")])

    sum_workload.short_description = "Сумма нагрузки (Занесённая)"

    def sum_workload_real(self, obj):
        return sum([x[0] for x in ScheduleItem.objects.filter(
            workload__teacher=obj).values_list("workload__workload")])

    sum_workload_real.short_description = "Сумма нагрузки (В рассписании)"

    list_display = ("id", "name", "sum_workload", "sum_workload_real")


class WorkloadAdmin(admin.ModelAdmin):

    list_display = ("id", "klass", "teacher", "workload", "lessons")

    list_filter = ("lessons", "klass", "teacher",)


class ScheduleItemAdmin(admin.ModelAdmin):

    list_display = ("id", "workload", "lesson_no", "date")

    list_filter = ("lesson_no", "date", "workload__teacher", "workload__klass")


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Workload, WorkloadAdmin)
admin.site.register(ScheduleItem, ScheduleItemAdmin)
