from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy
import django.utils as utils
from django.db import models
from datetime import datetime


class Position(models.Model):
    class Meta:
        db_table = 'position'
        verbose_name = 'Position of employee'

    title = models.CharField(max_length=100)
    duties = models.CharField(max_length=200)
    conditions = models.CharField(max_length=200)
    requirements = models.CharField(max_length=100)


class Document(models.Model):
    class Meta:
        db_table = 'document'
        verbose_name = 'Document'

    department_name = models.CharField(max_length=100)
    issue_date = models.DateField(default=datetime.now)
    expiration_date = models.DateField(default=None)


class Employee(models.Model):
    class Meta:
        db_table = 'employee'
        verbose_name = 'Employee'

    document = models.ForeignKey(Document, on_delete=models.RESTRICT)
    position = models.ForeignKey(Position, on_delete=models.RESTRICT)

    full_name = models.CharField(max_length=100)
    gender = models.BinaryField()
    birth_date = models.DateField()
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)


class Certificate(models.Model):
    class Meta:
        db_table = 'certificate'
        verbose_name = 'Certificate'

    account = models.ForeignKey(Employee, on_delete=models.CASCADE)

    issue_date = models.DateField(default=datetime.now)
    mark = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1),
        ],
    )


class Discipline(models.Model):
    class Meta:
        db_table = 'discipline'
        verbose_name = 'Discipline'

    employee = models.ForeignKey(Employee, on_delete=models.RESTRICT)

    title = models.CharField(max_length=100)
    hours = models.IntegerField()


class Exam(models.Model):
    class Meta:
        db_table = 'exam'
        verbose_name = 'Exam'

    discipline = models.ForeignKey(Discipline, on_delete=models.RESTRICT)

    attempts_count = models.IntegerField(default=0)
    type = models.CharField(max_length=20)

