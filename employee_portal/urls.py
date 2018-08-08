from django.urls import path
from . import views


app_name = 'employee_portal'
urlpatterns = [
    path('', views.Index_View.as_view(), name='index'),
    path('training_programs/', views.Training_Program_List_View.as_view(), name='training'),
    path('training_programs/<int:pk>', views.Training_Program_Detail_View.as_view(), name='training_detail'),
    path('training_programs/<int:pk>/edit', views.Training_Program_Edit_View.as_view(), name='edit_training'),
    path('training_programs/add', views.Training_Program_Add_View.as_view(), name='add_training')
]