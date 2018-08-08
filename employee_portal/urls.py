from django.urls import path
from django.views.generic import ListView

from . import views


app_name = 'employee_portal'
urlpatterns = [
    path('department/', views.DepartmentList.as_view(), name='department_list'),
    path('department/<int:pk>', views.DepartmentDetail.as_view(), name='department_detail'),
    # path('department/add', views.department_add, name='department_add'),
    # path('department/<int:pk>/edit', views.department_edit, name='department_edit'),
]