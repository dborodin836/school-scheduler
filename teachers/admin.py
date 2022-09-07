import datetime

from django.contrib import admin
from django.db.models import Sum

from lessons.models import ScheduleItem
from .models import Teacher, Workload


class TeacherAdmin(admin.ModelAdmin):

    def sum_workload(self, obj):
        first_available_date = datetime.date(year=datetime.date.today().year, month=9, day=4)
        last_available_date = first_available_date + datetime.timedelta(days=3)
        return ScheduleItem.objects.all().filter(workload__teacher=obj,
                                                 date__range=[first_available_date, last_available_date]).aggregate(Sum('workload__workload'))["workload__workload__sum"]

    list_display = ("id", "name", "sum_workload")


class WorkloadAdmin(admin.ModelAdmin):

    list_display = ("id", "klass", "teacher", "workload", "lessons")

    list_filter = ("lessons", "klass", "teacher",)


class ScheduleItemAdmin(admin.ModelAdmin):

    list_display = ("id", "workload", "lesson_no", "date")

    list_filter = ("lesson_no", "date", "workload__teacher", "workload__klass")


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Workload, WorkloadAdmin)
admin.site.register(ScheduleItem, ScheduleItemAdmin)
