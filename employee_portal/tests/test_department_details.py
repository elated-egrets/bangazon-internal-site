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

class Test_Department_Details(TestCase):
    """
        class to test the department details
    """

    def test_department_object_in_response(self):
        """ method to test department object is in response context and contains expected key and value pairs """

        response = self.client.get(reverse('employee_portal:department_detail'))

        self.assertEqual(len(response.context['department']), 1)

        self.assertIn(new_training_program.name.encode(), response.content)