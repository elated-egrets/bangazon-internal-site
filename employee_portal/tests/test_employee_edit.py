import unittest
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from employee_portal.models import Employee_Model, Departments, Training_Programs_Model


class Test_Training_Programs(TestCase):
    """
        module: test for employee edit
        author: Patrick Murphy
        purpose: testing the employee edit form
    """

    def test_employee_edit_view_can_be_submitted(self):
        """ method to test that we get a correct status code back from a put operation on employee edit """
        new_department = Departments.objects.create(
            name = "web development"
        )
        new_employee = Employee_Model.objects.create(
            first_name = "patrick",
            last_name = "murphy",
            department_id = new_department,
            end_date = "2019-02-02",
            is_supervisor = False,
        )

        response = self.client.get(reverse('employee_portal:employee_edit', kwargs={'pk':new_employee.id}))

        self.assertIn('<form action="/employees/"'.encode(), response.content)
        self.assertIn('<input type="text" name="first_name"'.encode(), response.content)
        self.assertIn('<input type="text" name="last_name"'.encode(), response.content)
        self.assertIn('<label for="id_department_id"'.encode(), response.content)
        self.assertIn('<label for="id_is_supervisor">'.encode(), response.content)
        self.assertIn('<label for="id_end_date">End date:</label>'.encode(), response.content)
