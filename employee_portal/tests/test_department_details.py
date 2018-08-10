import unittest
from django.test import TestCase
from django.urls import reverse
from employee_portal.models import Departments

"""
Your test suite must verify that a department object is in the response context
and contains the expected key and values.
    module: test for deparment model
    author: Patrick Murphy
    purpose: testing the department details
"""
test_department = Departments.objects.create()
class Test_Department_Details(TestCase):
    """
        class to test the department details
    """
    def test_list_department_details(self):
        """method to test employee detail can be created"""
        new_department = Departments.objects.create(
            name="coding department",
        )

        response = self.client.get(reverse('employee_portal:department_detail', kwargs={"pk":1}))
        self.assertEqual(response.status_code, 200)
