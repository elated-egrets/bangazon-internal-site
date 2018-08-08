from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView


class Index_View(TemplateView):
  template_name = 'employee_portal/index.html'
  # def location(self):
  #   return 'home'
  """
      The purpose of this class is to create the index page for the site. This just allows us to have a landing page where we can link to our other views.
  """
