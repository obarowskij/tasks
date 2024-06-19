from django.contrib import admin
from .models import Task
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.

@admin.register(Task)
class TaskAdmin(SimpleHistoryAdmin):
    pass
