from django.db import models
from django.db.models import Q
from .validators import validate_position
from django.core.exceptions import ObjectDoesNotExist


class Position(models.Model):
    name = models.CharField(max_length=150, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    salary = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)

    class Meta:
        db_table = "Position"

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return self.id


class Department(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        db_table = "Department"

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return self.id


class Employees(models.Model):

    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=100, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    employment_date = models.DateField(null=True)
    premium = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    image = models.ImageField(upload_to='profile_image', null=True, blank=True)

    class Meta:
        db_table = "Employees"

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)

    def is_image(self):
        if self.image:
            return True
        else:
            return False

    def get_image(self):
        return self.image.url

    def get_salary(self):
        res = (self.premium * self.get_position_salary())/100
        return "{0:.3f}".format(res + self.get_position_salary())

    def get_position_salary(self):
        return self.position.salary

    def get_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return self.id
