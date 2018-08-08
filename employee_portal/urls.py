from django.urls import path
from . import views


app_name = 'employee_portal'
urlpatterns = [
    path('', views.Index_View.as_view(), name='index'),
    path('training_programs/', views.Training_Program_List_View.as_view(), name='training')
]