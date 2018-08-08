from django.views.generic import DetailView
from employee_portal.models import Departments

"""
author: paul zimmerman-clayton

class view for Department Detail view
"""


class DepartmentDetail(DetailView):
  """
  summary: Class for DepartmentDetail view
  
  specifies Departments model for use in the department detail view
  names context object name as 'department'
  specifies template name as 'employee_portal/department_detail.html'
  """


  model = Departments
  context_object_name = 'department'
  template_name = 'employee_portal/department_detail.html'

