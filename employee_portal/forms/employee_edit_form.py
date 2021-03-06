from django import forms

from employee_portal.models import Employee_Model

from employee_portal.models import Training_Programs_Model

'''module: employee edit form
   author: Patrick Murphy
   purpose: form for editing an employee
'''
class Employee_Edit_Form(forms.ModelForm):
    '''this class with create the django form for adding an employee'''

    end_date = forms.DateField(required=False)
    training_program = forms.ModelMultipleChoiceField(required=False, queryset=Training_Programs_Model.objects.all())
    class Meta:
        model = Employee_Model
        fields = ('first_name', 'last_name','department_id','end_date', 'is_supervisor', 'training_program')