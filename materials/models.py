# materials/models.py
from django.db import models
from courses.models import Course

class StudyMaterial(models.Model):  # ✅ fixed spelling
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="materials",  # ✅ fixed spelling
        null=True,
        blank=True
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="materials/", blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.course.name})"