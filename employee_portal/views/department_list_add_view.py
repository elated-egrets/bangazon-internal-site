from django.views.generic import FormView
from employee_portal.forms import Department_Add_Form

"""
    module: department add view
    author: paul zimmerman-clayton
    purpose: to generate the view for adding a new department
"""

class Department_List_Add_View(FormView):
    template_name = 'employee_portal/department_add.html'
    form_class = Department_Add_Form
    success_url = '/departments/'

    def form_valid (self, form):
        form.save()
        return super(Department_List_Add_View, self).form_valid(form)
