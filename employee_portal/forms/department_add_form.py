from django import forms
from employee_portal.models import Departments_Model

"""
    module: department form
    author: paul zimmerman-clayton
    purpose: to handle creating the django form for adding a department
"""

class Department_Add_Form(forms.ModelForm):
    """
        this class wlil generate the django form for adding a department
    """
    
    class Meta:
        model = Departments_Model
        fields = ('name',)