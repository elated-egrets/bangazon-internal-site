from django.db import models

class Training_Programs_Model(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)