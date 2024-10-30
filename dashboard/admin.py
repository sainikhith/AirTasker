from django.contrib import admin

from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'completed','created_at', 'user']
    search_fields = ['user']

admin.site.register(Task,TaskAdmin)