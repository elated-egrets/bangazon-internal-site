from django.urls import path
from django.views.generic import ListView

from . import views


app_name = 'employee_portal'
urlpatterns = [
<<<<<<< HEAD
    path('departments/', views.DepartmentList.as_view(), name='department_list'),
    # path('department/<int:pk>', views.DepartmentDetail.as_view(), name='department_detail'),
    # path('department/add', views.department_add, name='department_add'),
    # path('department/<int:pk>/edit', views.department_edit, name='department_edit'),
    path('', views.Index_View.as_view(), name='index'),
    path('training_programs/', views.Training_Program_List_View.as_view(), name='training'),
    path('training_programs/add', views.Training_Program_Add_View.as_view(), name='add_training')
=======

    path('department/', views.DepartmentList.as_view(), name='department_list'),
    # path('department/<int:pk>', views.DepartmentDetail.as_view(), name='department_detail'),
    # path('department/add', views.department_add, name='department_add'),
    # path('department/<int:pk>/edit', views.department_edit, name='department_edit'),

    path('', views.Index_View.as_view(), name='index'),
    path('training_programs/', views.Training_Program_List_View.as_view(), name='training'),
    path('training_programs/add', views.Training_Program_Add_View.as_view(), name='add_training')

>>>>>>> 815899c4b81e79f8dc8f8d82ebb1f4079dc43717
]