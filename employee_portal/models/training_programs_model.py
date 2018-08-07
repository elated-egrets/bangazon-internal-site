from django.db import models

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
    """
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)