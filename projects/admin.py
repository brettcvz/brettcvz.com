from django.contrib import admin
from .models import Project


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'pubdate', 'visible', 'on_front_page')
    list_filter = ('pubdate', 'visible', 'on_front_page')
