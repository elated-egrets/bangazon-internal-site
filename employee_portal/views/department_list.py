from django.views.generic import ListView
from employee_portal.models import Departments

class DepartmentList(ListView):
  model = Departments
  # Django defaults to referencing the data in the template as 'object_list'. Here is how we can rename it what we want
  context_object_name = 'department_list'
  template_name = 'employee_portal/department_list.html'

  def department_list(self):  # NOTE that it's the method name that becomes the property on 'view'
    departments = Departments.objects.all()
    return departments