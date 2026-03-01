from django.shortcuts import render, get_object_or_404
from .models import Course
from subjects.models import Subject
from enrollments.models import Enrollment   


def course_index(request):
    """Show all courses across all subjects."""
    courses = Course.objects.select_related("subject", "teacher").all()

    enrolled_course_ids = []

    if request.user.is_authenticated and request.user.is_student:
        enrolled_course_ids = Enrollment.objects.filter(
            student=request.user   
        ).values_list("course_id", flat=True)

    context = {
        "courses": courses,
        "enrolled_course_ids": enrolled_course_ids,  
    }

    return render(request, "courses/course_index.html", context)


def course_list_by_subject(request, subject_id):
    """Show courses for a specific subject."""
    subject = get_object_or_404(Subject, id=subject_id)
    courses = Course.objects.filter(subject=subject).select_related("teacher")

    enrolled_course_ids = []

    if request.user.is_authenticated and request.user.is_student:
        enrolled_course_ids = Enrollment.objects.filter(
            student=request.user   # ✅ SAME HERE
        ).values_list("course_id", flat=True)

    context = {
        "subject": subject,
        "courses": courses,
        "enrolled_course_ids": enrolled_course_ids,  # ✅ SEND HERE TOO
    }

    return render(request, "courses/course_list.html", context)
