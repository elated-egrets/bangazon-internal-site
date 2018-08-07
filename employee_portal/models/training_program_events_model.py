from django.db import models
from .training_programs_model import Training_Programs_Model

class Training_Program_Events_Model(models.Model):
    training_program_id = models.ForeignKey(Training_Programs_Model, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    max_attendees = models.IntegerField()