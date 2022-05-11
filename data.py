import os
import django
from django.apps import apps
from django.db.models import Q
from datetime import datetime, timedelta
from random import randint, choice
from names import get_first_name, get_last_name
from django.core.exceptions import ObjectDoesNotExist

os.environ['DJANGO_SETTINGS_MODULE'] = 'company.settings'

django.setup()
Position = apps.get_model("employees", "Position")
Employee = apps.get_model('employees', 'Employees')
Department = apps.get_model('employees', 'Department')
pos = [
        {'name': 'Boss', 'parent': None, 'salary': 100.000, 'dept': 'Administration department'},
        {'name': 'Chief marketer', 'parent': 'Boss', 'salary': 80.000, 'dept': 'Administration department'},
        {'name': 'Head of Web Design', 'parent': 'Boss', 'salary': 95.000, 'dept': 'Administration department'},
        {'name': 'Head of Software Development', 'parent': 'Boss', 'salary': 95.000, 'dept': 'Administration department'},
        {'name': 'Senior Developer', 'parent': 'Head of Software Development', 'salary': 80.000, 'dept': 'Software development department'},
        {'name': 'Team Leader', 'parent': 'Head of Software Development', 'salary': 80.000, 'dept': 'Software development department'},
        {'name': 'Project Manager', 'parent': 'Head of Software Development', 'salary': 80.000, 'dept': 'Software development department'},
        {'name': 'Developer', 'parent': 'Head of Software Development', 'salary': 95.000, 'dept': 'Software development department'},
        {'name': 'Web Design', 'parent': 'Head of Web Design', 'salary': 80.000, 'dept': 'Web Design department'},
        {'name': 'Junior Developer', 'parent': 'Head of Software Development', 'salary': 80.000, 'dept': 'Software development department'},
    ]

list_post = ['Senior Developer', 'Team Leader', 'Project Manager', 'Developer', 'Project Manager', 'Developer', 'Junior Developer']
list_depart = ['Administration department', 'Software development department', 'Web Design department']


def create_position(name, parent, salary):
    Position = apps.get_model("employees", "Position")
    try:
        parent_ = Position.objects.get(name=parent)
    except ObjectDoesNotExist:
        parent_ = None
    position = Position(name=name,
                        parent=parent_,
                        salary=salary)
    position.save()


def create_dept(name):
    Department = apps.get_model('employees', 'Department')
    dept = Department(name=name)
    dept.save()


def create_employees(name, surname, position, department, employment_date, premium):
    Employees = apps.get_model('employees', 'Employees')
    emp = Employees(name=name,
                    surname=surname,
                    position=position,
                    department=department,
                    employment_date=employment_date,
                    premium=premium
                    )
    emp.save()


# for i in pos:
#     create_position(i['name'], i['parent'], i['salary'])
#
# for i in list_depart:
#     create_dept(i)

pos_boss = Position.objects.get(name='Boss')
dept = Department.objects.get(name='Administration department')
create_employees(get_first_name(), get_last_name(), pos_boss, dept,
                 (datetime.now() - timedelta(days=randint(1, 600))).date(),
                 randint(1, 20))

pos_soft = Position.objects.get(name='Chief marketer')
dept = Department.objects.get(name='Administration department')
create_employees(get_first_name(), get_last_name(), pos_soft, dept,
                 (datetime.now() - timedelta(days=randint(1, 600))).date(),
                 randint(1, 20))
#
pos_soft = Position.objects.get(name='Head of Web Design')
dept = Department.objects.get(name='Administration department')
create_employees(get_first_name(), get_last_name(), pos_soft, dept,
                 (datetime.now() - timedelta(days=randint(1, 600))).date(),
                 randint(1, 20))
#
pos_soft = Position.objects.get(name='Head of Software Development')
dept = Department.objects.get(name='Administration department')
create_employees(get_first_name(), get_last_name(), pos_soft, dept,
                 (datetime.now() - timedelta(days=randint(1, 600))).date(),
                 randint(1, 20))

for i in range(50000):
    name = choice(list_post)
    post_soft = Position.objects.get(name=name)
    print(post_soft)
    for t in pos:
        if name == t['name']:
            dept = Department.objects.get(name=t['dept'])

    create_employees(get_first_name(), get_last_name(), post_soft,
                        dept,
                        (datetime.now() - timedelta(days=randint(1, 600))).date(),
                        randint(1, 20))
