from django.views.generic import ListView
from employee_portal.models import Training_Programs_Model
"""
    module: training program list view
    author: riley mathews
    purpose: to generate the list view for training programs
"""


class Training_Program_List_View(ListView):
    """ This class will generate the view for listing out training programs """
    model = Training_Programs_Model
    template_name = 'employee_portal/training_program_list.html'
    context_object_name = 'training_list'