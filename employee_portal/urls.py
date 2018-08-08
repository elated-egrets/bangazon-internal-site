from django.urls import path
from . import views


app_name = 'employee_portal'
urlpatterns = [
    path('', views.Index_View.as_view(), name='index')
]