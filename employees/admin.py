from django.contrib import admin
from django import forms
from .models import Employees
from .models import Department
from .models import Position


class EmployeesAdmin(admin.ModelAdmin):
    # form
    list_display = ('name', 'surname', 'department', 'position', 'premium')
    list_filter = ('position', 'department')
    search_fields = ('name', 'position')

    class Meta:
        model = Employees


class DepartmentAdmin(admin.ModelAdmin):

    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

    class Meta:
        model = Department


class PositionAdmin(admin.ModelAdmin):

    list_display = ('name', 'parent')
    list_filter = ('name',)
    search_fields = ('name',)

    class Meta:
        model = Position


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Position, PositionAdmin)
