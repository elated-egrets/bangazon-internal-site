from django.views.generic import UpdateView
from employee_portal.models import Departments_Model
from employee_portal.forms import Department_Add_Form

"""
    module: employee edit view
    author: Patrick Murphy
    purpose: to generate a view for editing employee information
"""

class Department_Edit_View(UpdateView):
    model = Departments_Model
    form_class = Department_Add_Form
    success_url = '/departments/'
    template_name = 'employee_portal/department_add.html'