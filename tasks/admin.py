from django.contrib import admin
from .models import *


class TaskRecordInline(admin.TabularInline):
    model = TaskRecord

class RecurringPatternInline(admin.TabularInline):
    model = RecurringPattern

class TaskAdmin(admin.ModelAdmin):
    inlines = [
        TaskRecordInline,
        RecurringPatternInline
    ]

class TaskRecordAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at',)

# Register your models here.
admin.site.register(Task,TaskAdmin)
admin.site.register(TaskRecord, TaskRecordAdmin)
admin.site.register(RecurringPattern)
admin.site.register(UserProfileInfo)