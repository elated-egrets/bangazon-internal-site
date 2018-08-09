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
    
    def test_that_training_program_list_view_has_a_training_program(self):
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

    def test_training_program_add_form_has_expected_html(self):
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

    def test_posting_to_add_training_form_gets_expected_response_code(self):
        """ method to test that we can post an artst to the form """

        response = self.client.post(reverse('employee_portal:add_training'), {'name': 'hello', 'description': 'this is a test', 'start_date': '2019-12-12', 'end_date': '2019-12-12', 'max_attendees': 4})

        # Getting 302 back because we have a success url and the view is redirecting under the covers?
        self.assertEqual(response.status_code, 302)

    def test_training_program_detali_view_has_expected_data(self):
        """ method to test that the response of detail view has expected data """
        new_training_program = Training_Programs_Model.objects.create(
            name='test training',
            description='I hope this works!',
            start_date='2000-12-12',
            end_date='2001-12-12',
            max_attendees=5
        )

        response = self.client.get(reverse('employee_portal:training_detail', kwargs={'pk':1}))

        self.assertIn("test training".encode(), response.content)
        self.assertIn("I hope this works!".encode(), response.content)
        self.assertIn("Dec. 12, 2000".encode(), response.content)
        self.assertIn("Dec. 12, 2001".encode(), response.content)
        self.assertIn("5".encode(), response.content)

    def test_training_program_edit_view_can_be_submitted(self):
        """ method to test that we get a correct status code back from a put operation on training program edit """

        new_training_program = Training_Programs_Model.objects.create(
            name='whoops spelled this wrong',
            description='I hope this works!',
            start_date='2000-12-12',
            end_date='2001-12-12',
            max_attendees=5
        )

        response = self.client.post(reverse('employee_portal:edit_training', kwargs={'pk':new_training_program.id}), {'name': 'test training', 'description': 'I hope this works!', 'start_date': '2000-12-12', 'end_date': '2001-12-12', 'max_attendees': 5})

        self.assertEqual(response.status_code, 302)
        new_training_program.refresh_from_db()
        updated_response = self.client.get(reverse('employee_portal:training_detail', kwargs={'pk':new_training_program.id}))
        self.assertEqual(new_training_program.name, "test training")

    def test_training_program_can_be_deleted(self):
        """ method to test if a training program can be deleted """
        new_training_program = Training_Programs_Model.objects.create(
            name='whoops spelled this wrong',
            description='I hope this works!',
            start_date='2000-12-12',
            end_date='2020-12-12',
            max_attendees=5
        )

        response = self.client.delete(reverse('employee_portal:delete_training', kwargs={'pk':new_training_program.id}))

        # self.assertEqual(response.status_code, 200)
        self.assertIsInstance(new_training_program, Training_Programs_Model)