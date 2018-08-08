from django.urls import path

from employee_portal import views


app_name = 'employee_portal'
urlpatterns = [
    path('employees', views.Employee_List_View.as_view(), name='employee-list'),
]