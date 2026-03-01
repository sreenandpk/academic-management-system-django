from django.db import models
from django.contrib.auth import get_user_model
from courses.models import Course

User = get_user_model()

class Enrollment(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="enrollments"   # user.enrollments.all()
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="course_enrollments" , # course.course_enrollments.all()
        null=True,
        blank=True
    )
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "course")  # prevent duplicate enrollments

    def __str__(self):
        return f"{self.student.username} → {self.course.name}"