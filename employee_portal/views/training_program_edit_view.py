from django.views.generic import UpdateView
from employee_portal.models import Training_Programs_Model
from employee_portal.forms import Training_Program_Add_Form

"""  
    module: training program edit view
    author: riley mathews
    purpose: to generate a view for updating training program information
"""

class Training_Program_Edit_View(UpdateView):
    model = Training_Programs_Model
    form_class = Training_Program_Add_Form
    success_url = '/training_programs/'