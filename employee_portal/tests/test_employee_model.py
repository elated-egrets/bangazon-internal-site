import unittest
from django.test import TestCase
from django.urls import reverse
# from django.utils import timezone
from employee_portal.models import Employee_Model
from employee_portal.models import Departments_Model

"""
    module: test for Employee model
    author: Ronnie Young
    purpose: testing the Employee model
"""
test_department = Departments_Model.objects.create()
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

