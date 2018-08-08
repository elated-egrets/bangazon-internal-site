from django.db import models
from .employee_model import Employee_Model
from .training_programs_model import Training_Programs_Model

"""
    module: employee training
    author: riley mathews
    purpose: to hold the model for employee training
"""

class Employee_Trainings_Model(models.Model):
    """
        This class is the intersection table from employees to training programs

        fields:
            employee_id - foreign key, reference to employee table
            training_program_id - foreign key, reference to training program table
    """
    employee_id = models.ForeignKey(Employee_Model, on_delete=models.CASCADE)
    training_program_id = models.ForeignKey(Training_Programs_Model, on_delete=models.CASCADE)