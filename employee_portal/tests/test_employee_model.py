import unittest
from django.test import TestCase
from django.urls import reverse
# from django.utils import timezone
from employee_portal.models import Employee_Model
from employee_portal.models import Departments

"""
    module: test for Employee model
    author: Ronnie Young
    purpose: testing the Employee model
"""
test_department = Departments.objects.create()
class Test_Employee_Models(TestCase):
    """
        class to test the Employee model
    """
    def test_list_employee_models(self):
        """method to test employee model can be created"""
        new_employee = Employee_Model.objects.create(
            first_name="Richard",
            last_name="What",
            department_id=test_department,
            # start_date=timezone.now(),
            end_date="2022-06-01",
            is_supervisor=False
        )

    #     response = self.client.get(reverse('employee_portal:employee'))

    #     self.assertEqual(len(response.context['employee_list']), 1)

    #     self.assertIn(new_training_program.name.encode(), response.content)


    # def test_post_artist(self):
    #     """ method to test that we can post an employee to the form """

    #     response = self.client.post(reverse('employee_portal:add_employee'), {'name': 'hello', 'description': 'this is a test', 'start_date': '2019-12-12', 'end_date': '2019-12-12', 'max_attendees': 4})

    #     # Getting 302 back because we have a success url and the view is redirecting under the covers?
    #     self.assertEqual(response.status_code, 302)