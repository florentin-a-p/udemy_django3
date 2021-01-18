from django.contrib import admin
from .models import ProjectTodoWooFlo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('memo_created_date',)

admin.site.register(ProjectTodoWooFlo,TodoAdmin)
