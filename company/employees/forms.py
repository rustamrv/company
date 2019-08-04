from django import forms

from .models import Employees, Department, Position


class DateInput(forms.DateInput):
    input_type = 'date'


class EmployeesForm(forms.ModelForm):

    class Meta:
        model = Employees
        fields = '__all__'
        widgets = {
            'employment_date':  DateInput(attrs={'type': 'date'})
        }