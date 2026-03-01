# subjects/models.py
from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)   # unique subject name
    description = models.TextField(blank=True, null=True)  # optional description

    def __str__(self):
        return self.name