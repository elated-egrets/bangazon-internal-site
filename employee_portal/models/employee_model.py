from django.db import models
from django.utils import timezone

class Employee(models.Model):
    """[Model for employee table
        This model is used for employee information]

    Data:
        first_name --- The Employee's first name.
        last_name --- The Employee's last name.
        department_id --- The id of the department.
        state_date --- The employee's start date.
        end_date --- The employee's end date.
        is_supervisor --- Is the person a supervisor or not.
    """

    first_name = models.CharField(max_length = 10)
    last_name = models.CharField(max_length = 10)
    department_id = models.ForeignKey(Department, related_name="department", on_delete=models.CASCADE)
    state_date = timezone.now()
    end_date = models.DateField()
    is_supervisor = models.BooleanField(default=False)

    def __str__(self):
        """A string representation of the Employee.

           Returns:
           string --- employee name and then description of said employee.
        """

    return f'{self.first_name} {self.last_name} {department_id}'


# from django.db import models
# from safedelete.models import SafeDeleteModel, SOFT_DELETE
# from safedelete.managers import SafeDeleteManager
# from safedelete import DELETED_VISIBLE_BY_PK

# class MyModelManager(SafeDeleteManager):
#     _safedelete_visibility = DELETED_VISIBLE_BY_PK

# class Category(SafeDeleteModel):
#     '''Model for the categories.

#     Data:
#       name --- name representation of the category
#       description --- description of the category
#     '''
#     _safedelete_policy = SOFT_DELETE
#     objects = MyModelManager()
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=400)

#     def __str__(self):
#       '''A string representation of the Category.

#       Returns:
#         string --- category name and then description of said category.
#       '''
#       return f'{self.name}: {self.description}'