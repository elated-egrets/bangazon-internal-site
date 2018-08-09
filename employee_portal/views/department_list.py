from django.views.generic import ListView
from employee_portal.models import Departments_Model

"""
author: paul zimmerman-clayton

class view for Department List view
"""


class DepartmentList(ListView):
  """
  summary: Class for DepartmentList view
  
  specifies Departments_Model model for use in the department list view
  names context object name as 'department_list'
  specifies template name as 'employee_portal/department_list.html'
  """


  model = Departments_Model
  context_object_name = 'department_list'
  template_name = 'employee_portal/department_list.html'

  # def department_list(self):
  #   """
  #   [summary]
    
  #   Returns:
  #     [type] -- [description]
  #   """
  #   departments = Departments_Model.objects.all()

  #   return departments