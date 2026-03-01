# materials/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import StudyMaterial
from courses.models import Course
from .forms import StudyMaterialForm

@login_required
def upload_material(request, course_id):
    course = get_object_or_404(Course, id=course_id, teacher=request.user)
    if request.method == "POST":
        form = StudyMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.course = course
            material.save()
            messages.success(request, "Material uploaded successfully.")
            return redirect("teachers:teacher_course_materials", course_id=course.id)

    else:
        form = StudyMaterialForm()
    return render(request, "materials/upload.html", {"form": form, "course": course})

@login_required
def course_materials(request, course_id):
    if not request.user.is_student:
        return render(request, "403.html")  # or redirect to a safe page

    course = get_object_or_404(Course, id=course_id)
    materials = StudyMaterial.objects.filter(course=course)

    return render(request, "materials/list.html", {
        "course": course,
        "materials": materials,
    })

    