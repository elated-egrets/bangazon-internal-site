from django.utils import timezone
from django.views.generic.list import ListView

from employee_portal import models

'''module: employee list view
   author: Jonny Riggs
   purpose: to generate a list view of all the employees
'''
class Employee_List_View(ListView):
    '''This class will generate a list of the employees

    Arguments:
        ListView {[view]} -- taking the employee model and using ListView for generating the list

    Returns:
        http request -- submits the list for that url request
    '''

    model = models.Employee_Model
    template_name = 'employee_portal/employee_model_list.html'
    context_object_name = 'employee_list'