from django.db import models

class Libro(models.Model):
    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)