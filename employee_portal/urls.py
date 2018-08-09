from django.urls import path

from employee_portal import views
from . import views


app_name = 'employee_portal'
urlpatterns = [
    path('employees/', views.Employee_List_View.as_view(), name='employee_list'),
    path('', views.Index_View.as_view(), name='index'),
    path('training_programs/', views.Training_Program_List_View.as_view(), name='training'),
    path('training_programs/add', views.Training_Program_Add_View.as_view(), name='add_training')

]