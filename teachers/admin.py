from django.contrib import admin

from .models import Teacher, Workload


class TeacherAdmin(admin.ModelAdmin):

    list_display = ("id", "name")


class WorkloadAdmin(admin.ModelAdmin):

    list_display = ("id", "klass", "teacher", "workload")


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Workload, WorkloadAdmin)
