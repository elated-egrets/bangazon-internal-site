import unittest
from django.test import TestCase
from django.urls import reverse
# from django.utils import timezone
from employee_portal.models import Employee_Model
from employee_portal.models import Departments

"""
    module: test for Employee model
    author: Jonny Riggs
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
            first_name="Jonny",
            last_name="Riggs",
            department_id=test_department,
            # start_date=timezone.now(),
            end_date="2022-06-01",
            is_supervisor=False
        )

        response = self.client.get(reverse('employee_portal:employee_list'))

        self.assertEqual(len(response.context['employee_list']), 1)

    def test_employee_list_template(self):
        '''method to test the emplyee template'''

        response = self.client.get(reverse('employee_portal:employee_list'))

        self.assertIn('<h1>Employees</h1>'.encode(), response.content)

    def test_employee_content(self):
        '''method to test the employee content'''

        new_employee = Employee_Model.objects.create(
            first_name="Jonny",
            last_name="Riggs",
            department_id=test_department,
            # start_date=timezone.now(),
            end_date="2022-06-01",
            is_supervisor=False
        )
        response = self.client.get(reverse('employee_portal:employee_list'))

        self.assertIn('Jonny'.encode(), response.content)