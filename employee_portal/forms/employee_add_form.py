from django import forms

from employee_portal.models import Employee_Model

'''module: employee add form
   author: Jonny Riggs
   purpose: form for adding an employee
'''

class Employee_Add_Form(forms.ModelForm):
    '''this class with create the django form for adding an employee'''

    class Meta:
        model = Employee_Model
        fields = ('first_name', 'last_name','department_id','is_supervisor', )