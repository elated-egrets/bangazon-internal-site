from django import forms
from employee_portal.models import Training_Programs_Model

"""  
    module: training program form
    author: riley mathews
    purpose: to handle creating the django form for adding a training program
"""

class Training_Program_Add_Form(forms.ModelForm):
    """this class will generate the django form for adding a training program"""
    class Meta:
        model = Training_Programs_Model
        fields = ('name', 'description', 'start_date', 'end_date', 'max_attendees')