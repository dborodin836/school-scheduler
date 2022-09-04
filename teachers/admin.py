from django.contrib import admin

from lessons.models import ScheduleItem
from .models import Teacher, Workload


class TeacherAdmin(admin.ModelAdmin):

    list_display = ("id", "name")


class WorkloadAdmin(admin.ModelAdmin):

    list_display = ("id", "klass", "teacher", "workload", "lessons")


class ScheduleItemAdmin(admin.ModelAdmin):

    list_display = ("id", "workload", "lesson_no", "date")

    list_filter = ("lesson_no", "date")


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Workload, WorkloadAdmin)
admin.site.register(ScheduleItem, ScheduleItemAdmin)
