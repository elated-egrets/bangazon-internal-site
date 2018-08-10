from django.urls import path
from employee_portal import views
from django.views.generic import ListView
from . import views


app_name = 'employee_portal'
urlpatterns = [
    path('', views.Index_View.as_view(), name='index'),
    path('training_programs/', views.Training_Program_List_View.as_view(), name='training'),
    path('training_programs/add', views.Training_Program_Add_View.as_view(), name='add_training'),
    path('employees/<int:pk>/', views.Employee_Detail_View.as_view(), name="employee_detail"),
    path('employees/', views.Employee_List_View.as_view(), name='employee_list'),
    path('departments/', views.DepartmentList.as_view(), name='department_list'),
    path('departments/add', views.Department_List_Add_View.as_view(), name='add_department'),
    path('departments/<int:pk>', views.Department_Detail_View.as_view(), name='department_detail'),
    # path('department/<int:pk>/edit', views.department_edit, name='department_edit'),
    path('', views.Index_View.as_view(), name='index'),
    path('training_programs/', views.Training_Program_List_View.as_view(), name='training'),
    path('training_programs/<int:pk>', views.Training_Program_Detail_View.as_view(), name='training_detail'),
    path('training_programs/<int:pk>/edit', views.Training_Program_Edit_View.as_view(), name='edit_training'),
    path('training_programs/add', views.Training_Program_Add_View.as_view(), name='add_training'),
    path('employees/add', views.Employee_Add_View.as_view(), name='add_employee'),
    path('training_programs/<int:pk>/delete', views.Training_Program_Delete_View.as_view(), name='delete_training')]