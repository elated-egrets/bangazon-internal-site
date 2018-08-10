import unittest
from django.test import TestCase
from django.urls import reverse
# from django.utils import timezone
from employee_portal.models import Employee_Model
from employee_portal.models import Departments

"""module: test to add an employee
   author: Jonny Riggs
   purpose: test to see that an employee has been added.
"""
test_department = Departments.objects.create()

class Test_Employee_Add(TestCase):

    def test_employee_add_form_has_html(self):
        '''method for testing to make sure that the form for adding an employee is getting the expected data
        '''

        response = self.client.get(reverse('employee_portal:add_employee'))

        self.assertIn('<form action="/employees/"'.encode(), response.content)
        self.assertIn('<input type="submit" value="Employees"'.encode(), response.content)
        self.assertIn('<input type="submit" value="Training Programs"'.encode(), response.content)
        self.assertIn('<input type="submit" value="Departments"'.encode(), response.content)
        self.assertIn('<input type="text" name="first_name" maxlength="10" required id="id_first_name"'.encode(), response.content)
        self.assertIn('<input type="text" name="last_name" maxlength="10" required id="id_last_name"'.encode(), response.content)
        self.assertIn('<select name="department_id" required id="id_department_id"'.encode(), response.content)
        self.assertIn('<input type="text" name="end_date" required id="id_end_date"'.encode(), response.content)
        self.assertIn('<input type="checkbox" name="is_supervisor" id="id_is_supervisor"'.encode(), response.content)
