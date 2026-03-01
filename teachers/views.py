from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from courses.models import Course
from enrollments.models import Enrollment
from materials.models import StudyMaterial

@login_required
def dashboard(request):
    # Show only courses owned by this teacher
    courses = Course.objects.filter(teacher=request.user)
    return render(request, "teachers/dashboard.html", {"courses": courses})

@login_required
def teacher_profile(request):
    user = request.user

    # Safety: Only allow teachers
    if not user.is_teacher:
        return render(request, "403.html")  # or redirect somewhere

    # Show courses taught by this teacher
    courses = Course.objects.filter(teacher=user)

    context = {
        "user": user,
        "courses": courses
    }
    return render(request, "teachers/profile.html", context)

@login_required
def course_students(request, course_id):
    # Ensure the course belongs to the logged-in teacher
    course = get_object_or_404(Course, id=course_id, teacher=request.user)

    # Get all enrollments for this course
    students = Enrollment.objects.filter(course=course)

    return render(request, "teachers/course_students.html", {
        "course": course,
        "students": students,
    })


@login_required
def teacher_course_materials(request, course_id):
    # Ensure the course belongs to the logged-in teacher
    course = get_object_or_404(Course, id=course_id, teacher=request.user)

    # Get all materials for this course
    materials = StudyMaterial.objects.filter(course=course)

    return render(request, "teachers/course_materials.html", {
        "course": course,
        "materials": materials,
    })
