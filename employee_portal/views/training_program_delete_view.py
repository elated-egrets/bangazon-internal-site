from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from employee_portal.models import Training_Programs_Model

"""  
    module: training program delete view
    author: riley mathews
    purpose: to make a view that will delete the appropiate training program
"""

class Training_Program_Delete_View(DeleteView):
    """ class to create the view that will be used for deleting a training program """

    model = Training_Programs_Model
    success_url = reverse_lazy('employee_portal:training')
    template_name = 'employee_portal/training_program_delete.html'

    def delete(self, request, *args, **kwargs):
        print('tried to delete!')
        return HttpResponseRedirect(reverse_lazy('employee_portal:training'))
        # return super(Training_Program_Delete_View, self).delete(request, *args, **kwargs)