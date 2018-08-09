from django.views.generic import DetailView
from employee_portal.models import Training_Programs_Model

"""  
    module: training program detail view
    author: riley mathews
    purpose: to generate a view for training program detail view page
"""

class Training_Program_Detail_View(DetailView):
    model = Training_Programs_Model
    template_name = 'employee_portal/training_program_detail.html'
    context_object_name = 'training'