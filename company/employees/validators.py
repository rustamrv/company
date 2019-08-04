from django.core.exceptions import ValidationError
from django.apps import apps
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


def validate_position(value):
    position = apps.get_model("employees", "Position")
    employees = apps.get_model('employees', 'Employees')
    print(value)
    try:
        emp_get = employees.objects.get(position=position.objects.get(name='Boss'))
    except employees.MultipleObjectsReturned:
        emp_get = None
    except ObjectDoesNotExist:
        emp_get = ""
    # res = employees.objects.get(position=position.objects.get(name=value))

    if emp_get is None:
        raise ValidationError('The boss is already there')


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )