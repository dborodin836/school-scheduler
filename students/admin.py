from django.contrib import admin

from .models import Class


class ClassAdmin(admin.ModelAdmin):
    list_display = ("id", "year", "letter_id")


admin.site.register(Class, ClassAdmin)
