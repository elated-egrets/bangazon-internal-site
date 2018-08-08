from django.utils import timezone
from django.views.generic.list import ListView

from employee_portal import models

class Employee_List_View(ListView):
    model = models.Employee_Model

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context