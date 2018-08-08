import unittest
from django.test import TestCase
from django.urls import reverse
from employee_portal.models import Training_Programs_Model

""" 
    module: test for training program model
    author: riley mathews
    purpose: testing the training program model
"""

class Test_Training_Programs(TestCase):
    """ 
        class to test the training programs model
    """
    
    def test_list_training_programs(self):
        new_training_program = Training_Programs_Model.objects.create(
            name='test training',
            description='I hope this works!',
            start_date='2000-12-12',
            end_date='2001-12-12',
            max_attendees=5
        )

        response = self.client.get(reverse('employee_portal:training'))

        self.assertEqual(len(response.context['training_list']), 1)

    
    