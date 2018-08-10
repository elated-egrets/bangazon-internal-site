from django.views.generic import FormView

from django.urls import reverse_lazy

from employee_portal.forms import Employee_Add_Form

from employee_portal.models import Employee_Model

'''module: employee add view
   author: Jonny Riggs
   purpose: to add a new employee to the list and the database
'''
class Employee_Add_View(FormView):
    template_name = 'employee_portal/employee_add.html'
    form_class = Employee_Add_Form
    success_url = reverse_lazy('employee_portal:employee_list')

    def form_valid(self, form):
        """this method will submit the form for adding an employee

        Arguments:
            form --  passed in from form submission

        Returns:
            http request -- submits the form for adding an employee
        """
        form.save()
        return super(Employee_Add_View, self).form_valid(form)