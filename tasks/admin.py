from django.contrib import admin
from .models import Task

# Register your models here.

class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created', 'date_completed', 'important', 'user')

admin.site.register(Task, TasksAdmin)