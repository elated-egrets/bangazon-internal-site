import unittest
from django.test import TestCase
from django.urls import reverse
from employee_portal.models import Departments_Model


"""
    module: test for department model
    author: paul zimmerman-clayton
    purpose: testing the department model
"""

class Test_Departments_Model(TestCase):
    """
    class to test the departments model
    """
    
    def test_departments_context(self):
        """method to test department can be created
        """
        new_department = Departments_Model.objects.create(
            name='test department'
        )

        response = self.client.get(reverse('employee_portal:department_list'))
        
        """tests to make sure there is only one item created
        """

        self.assertEqual(len(response.context['department_list']), 1)

        """tests to make sure the name is what is expected
        """

        self.assertIn(new_department.name.encode(), response.content)

    def test_department_add_form_has_expected_field(self):
        """tests to see if the department add form has the required input field
        """

        response = self.client.get(reverse('employee_portal:add_training'))

        self.assertIn('<form action="/training_programs"'.encode(), response.content)
        self.assertIn('<input type="text" name="name" maxlength="40" required id="id_name"'.encode(), response.content)

    def test_posting_to_add_department_gets_expected_response_code(self):
        """Checks response of add department form (200 expected)
        """


        response = self.client.post(reverse('employee_portal:add_training'))

        self.assertEqual(response.status_code, 200)