from django.contrib import admin
from firstapp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'eno', 'ename', 'eaddr', 'esal']


admin.site.register(Employee, EmployeeAdmin)