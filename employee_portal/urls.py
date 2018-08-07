from django.urls import path
# from 

from . import views


app_name = 'employee_portal'
urlpatterns = [
    path('department', views.department_list),
    path('department/<pk:id>', views.department_detail, name='department_detail'),
    path('department/add', views.department_add, name='department_add'),
    path('department/<pk:id>/edit', views.department_edit, name='department_edit'),
]