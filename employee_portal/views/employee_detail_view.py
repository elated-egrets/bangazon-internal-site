from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView
from employee_portal.models import Employee_Model
# from employee_portal.models import Departments

# class Employee_Detail_View(TemplateView):
#   """
#       The purpose of this class is to create the detail view page for the site. This allows us to click on the employee name and view their detials.
#   """
#   template_name = 'employee_portal/employee_detail.html'
  # def location(self):
  #   return 'home'

class Employee_Detail_View(DetailView):
    """
      The purpose of this class is to create the detail view page for the site. This allows us to click on the employee name and view their details.
    """
    model = Employee_Model
    template_name = 'employee_portal/employee_detail.html'

# class Employee_Department_View(DetailView):
#     model = Departments