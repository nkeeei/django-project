from django.contrib import admin

from .models import Task


class MyModelAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Task, MyModelAdmin)
