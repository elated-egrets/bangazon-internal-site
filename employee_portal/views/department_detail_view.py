from django.views.generic import DetailView
from employee_portal.models import Departments_Model

class Department_Detail_View(DetailView):
  """
  summary: Class for Department_Detail view
  author: Patrick Murphy
  specifies Departments model for use in the department list view
  names context object name as 'department'
  specifies template name as 'employee_portal/department_detail.html'
  """

  model = Departments_Model
  context_object_name = 'department'
  template_name = 'employee_portal/department_detail.html'
