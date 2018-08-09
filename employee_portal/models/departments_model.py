from django.db import models

"""
    module: departments model
    author: paul zimmerman-clayton
    purpose: data model for departments

"""


class Departments_Model_Model(models.Model):
    """
        This model holds the data for Bangazon Departments_Model.

        fields:
            name - string. name of the department. max length: 20. 

    """

    name = models.CharField(max_length=20)