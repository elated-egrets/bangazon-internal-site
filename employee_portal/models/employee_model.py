from django.db import models
from django.utils import timezone
from .departments_model import Departments
from .training_programs_model import Training_Programs_Model

class Employee_Model(models.Model):
    """[Model for employee table
        This model is used for employee information]

    Data:
        first_name --- The Employee's first name.
        last_name --- The Employee's last name.
        department_id --- The id of the department.
        state_date --- The employee's start date.
        end_date --- The employee's end date.
        is_supervisor --- Is the person a supervisor or not.
        training_program --- many to many field with training program table
    """

    first_name = models.CharField(max_length = 10)
    last_name = models.CharField(max_length = 10)
    department_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
    start_date = timezone.now()
    end_date = models.DateField()
    is_supervisor = models.BooleanField(default=False)
    training_program = models.ManyToManyField(Training_Programs_Model, related_name="training_program")

    def __str__(self):
        """A string representation of the Employee.

           Returns:
           string --- employee name and then description of said employee.
        """

        return f'{self.first_name} {self.last_name} {self.department_id}'

