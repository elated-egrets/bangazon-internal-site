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