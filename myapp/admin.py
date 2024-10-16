from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','course','registration_number','registration_date')
    search_fields = ('first_name', 'course', 'registration_number')
    list_filter = ('registration_number', 'course')
    