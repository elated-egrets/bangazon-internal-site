from django.views.generic import UpdateView
from employee_portal.models import Training_Programs_Model, Employee_Model
from employee_portal.forms import Employee_Edit_Form

"""
    module: employee edit view
    author: Patrick Murphy
    purpose: to generate a view for editing employee information
"""

class Employee_Edit_View(UpdateView):
    model = Employee_Model
    form_class = Employee_Edit_Form
    success_url = '/employees/'
    template_name = 'employee_portal/employee_edit.html'