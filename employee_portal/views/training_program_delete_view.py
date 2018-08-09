from django.views.generic import DeleteView
from django.urls import reverse
from employee_portal.models import Training_Programs_Model

"""  
    module: training program delete view
    author: riley mathews
    purpose: to make a view that will delete the appropiate training program
"""

class Training_Program_Delete_View(DeleteView):
    """ class to create the view that will be used for deleting a training program """

    model = Training_Programs_Model
    success_url = '/training_programs/'
    # success_url = reverse('employee_portal:training')
    template_name = 'employee_portal/training_program_delete.html'