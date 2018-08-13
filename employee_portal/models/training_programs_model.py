from django.db import models
# from django.db import migrations

# class Migration(migrations.Migration):
#     atomic = False

"""
    module: training programs model
    author: riley mathews
    purpose: to create the data model for training programs
"""

class Training_Programs_Model(models.Model):
    """
        The purpose of this class is to create the data model
        for employee training programs. This class does not
        create the individual sessions for programs
        instead its purpose is to hold the name and description
        for a training program that can be repeated many times over
        without repeating data.

        Fields:
            name - string, max length 40 characters
            description - string, max length 200 characters
            start_date - date, start date of the event
            end_date - date, end date of the event
            max_attendees - integer, maximum people who can attend the event
    """
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    max_attendees = models.IntegerField()

    def __str__(self):


        return f'{self.name}'