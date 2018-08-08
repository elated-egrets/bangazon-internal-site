from django.views.generic import FormView
from employee_portal.forms import Training_Program_Add_Form

""" module: training program add view
    author: riley mathews
    purpose: to generate the view for adding a new training program """

class Training_Program_Add_View(FormView):
    """ This class will generate the view for adding a new training program """
    template_name = 'employee_portal/training_program_add.html'
    form_class = Training_Program_Add_Form
    success_url = '/training_programs/'

    def form_valid(self, form):
        """this method will submit the form
        
        Arguments:
            form {form} -- auto passed in from form submission
        
        Returns:
            http request -- submits the form
        """
        form.save()
        return super(Training_Program_Add_View, self).form_valid(form)