import unittest
from django.test import TestCase
from django.urls import reverse
# from django.utils import timezone
from employee_portal.models import Employee_Model
from employee_portal.models import Departments_Model

"""
    module: test for Employee Details
    author: Ronnie Young
    purpose: testing the Employee Details
"""

test_department = Departments_Model.objects.create()
class Test_Employee_Details(TestCase):
    """
        class to test the Employee Details
    """
    def test_list_employee_details(self):
        """method to test employee detail can be created"""
        new_employee = Employee_Model.objects.create(
            first_name="Richard",
            last_name="What",
            department_id=test_department,
            # start_date=timezone.now(),
            end_date="2022-06-01",
            is_supervisor=False
        )

        response = self.client.get(reverse('employee_portal:employee_detail', kwargs={"pk":1}))
        self.assertEqual(response.status_code, 200)

        # Is this stuff in the content of the body?
        # .encode converts from unicode to utf-8
        # example:
        # If the string is: pythön!
        # The encoded version is: b'pyth\xc3\xb6n!'
        # self.assertIn(new_employee.first_name.encode(), response.content)
        # self.assertIn(new_employee.last_name.encode(), response.content)
