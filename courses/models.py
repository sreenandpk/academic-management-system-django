from django.db import models
from django.contrib.auth import get_user_model
from subjects.models import Subject

User = get_user_model()

class Course(models.Model):
    name = models.CharField(max_length=100)                # Course title
    description = models.TextField()                       # Details about the course
    
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="courses",
        null=True,
        blank=True
    )

    image = models.ImageField(upload_to="course_images/", blank=True, null=True)  # NEW

    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="courses",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)   # When course was created
    updated_at = models.DateTimeField(auto_now=True)       # Last update time

    def __str__(self):
        return self.name