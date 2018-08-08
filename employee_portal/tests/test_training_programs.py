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
        """ method to test training program can be created """
        new_training_program = Training_Programs_Model.objects.create(
            name='test training',
            description='I hope this works!',
            start_date='2000-12-12',
            end_date='2001-12-12',
            max_attendees=5
        )

        response = self.client.get(reverse('employee_portal:training'))

        self.assertEqual(len(response.context['training_list']), 1)

        self.assertIn(new_training_program.name.encode(), response.content)

    def test_training_programs_add(self):
        """ method to test form for adding a training program """

        response = self.client.get(reverse('employee_portal:add_training'))

        self.assertIn('<form action="/employees/"'.encode(), response.content)
        self.assertIn('<input type="submit" value="Employees"'.encode(), response.content)
        self.assertIn('<input type="submit" value="Training Programs"'.encode(), response.content)
        self.assertIn('<input type="submit" value="Departments"'.encode(), response.content)
        self.assertIn('<input type="text" name="name" maxlength="40" required id="id_name"'.encode(), response.content)
        self.assertIn('<input type="text" name="description" maxlength="200" required id="id_description"'.encode(), response.content)
        self.assertIn('<input type="text" name="start_date" required id="id_start_date"'.encode(), response.content)
        self.assertIn('<input type="text" name="end_date" required id="id_end_date"'.encode(), response.content)
        self.assertIn('<input type="number" name="max_attendees" required id="id_max_attendees"'.encode(), response.content)
        self.assertIn('<input type="submit" value="Add Program"'.encode(), response.content)

    def test_post_artist(self):
        """ method to test that we can post an artst to the form """

        response = self.client.post(reverse('employee_portal:add_training'), {'name': 'hello', 'description': 'this is a test', 'start_date': '2019-12-12', 'end_date': '2019-12-12', 'max_attendees': 4})

        # Getting 302 back because we have a success url and the view is redirecting under the covers?
        self.assertEqual(response.status_code, 302)

    
    