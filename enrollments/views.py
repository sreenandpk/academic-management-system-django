from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Enrollment
from courses.models import Course

@login_required
def enroll(request, course_id):
    """Enroll the logged-in student in a course."""
    course = get_object_or_404(Course, id=course_id)
    Enrollment.objects.get_or_create(student=request.user, course=course)
    return redirect("students:dashboard")

@login_required
def enrollment_list(request):
    """Show all courses the logged-in student is enrolled in."""
    enrollments = request.user.enrollments.select_related("course__subject")
    return render(request, "enrollments/enrollment_list.html", {"enrollments": enrollments})