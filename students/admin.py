from django.contrib import admin
from .models import Student


class ProjectAdmin(admin.ModelAdmin):
    


# Register your models here.
    admin.site.register(Student)