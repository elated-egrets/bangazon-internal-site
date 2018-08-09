import unittest
from django.test import TestCase
from django.urls import reverse
# from django.utils import timezone
from employee_portal.models import Employee_Model
from employee_portal.models import Departments

"""
    module: test for Employee Details
    author: Ronnie Young
    purpose: testing the Employee Details
"""

test_department = Departments.objects.create()
class Test_Employee_Details(TestCase):
    """
        class to test the Employee Details
    """
    def test_list_employee_details(self):
        """method to test employee detail can be created"""
        new_employee = Employee_Details.objects.create(
            first_name="Richard",
            last_name="What",
            department_id=test_department,
            # start_date=timezone.now(),
            end_date="2022-06-01",
            is_supervisor=False
        )


        # Is this stuff in the content of the body?
        # .encode converts from unicode to utf-8
        # example:
        # If the string is: pythön!
        # The encoded version is: b'pyth\xc3\xb6n!'
        self.assertIn(new_employee.first_name.encode(), response.content)
        self.assertIn(new_employee.last_name.encode(), response.content)