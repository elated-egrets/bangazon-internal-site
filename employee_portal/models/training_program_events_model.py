from django.db import models

from .training_programs_model import Training_Programs_Model

"""
    module: training program events model
    author: riley mathews
    purpose: to create the data model for training prgram events
"""

class Training_Program_Events_Model(models.Model):
    """
        This model holds the data for training program events.
        It pulls the data for the information of the particular
        event from the training programs model, and creates
        individual instances of that particular program.

        fields:
            training_program_id - foreign key, links to training program model
            start_date - date, the date the program will start
            end_date - date, the date the program will end
            max_attendees - integer, the maximum number of people who can attend the program session
    """
    training_program_id = models.ForeignKey(Training_Programs_Model, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    max_attendees = models.IntegerField()