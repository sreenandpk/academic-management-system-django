from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from enrollments.models import Enrollment
from accounts.forms import ProfileImageForm

@login_required
def dashboard(request):
    if not request.user.is_student:
        return redirect("accounts:login")

    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, "students/dashboard.html", {
        "enrollments": enrollments
    })

@login_required
def student_profile(request):
    user = request.user

    # Safety: Only allow students
    if not getattr(user, "is_student", False):
        return render(request, "403.html")

    enrollments = Enrollment.objects.filter(student=user)
    profile = user.profile   # OneToOne Profile

    if request.method == "POST":
        form = ProfileImageForm(
            request.POST,
            request.FILES,
            instance=profile
        )
        if form.is_valid():
            form.save()
            return redirect("students:student_profile")
    else:
        form = ProfileImageForm(instance=profile)

    context = {
        "user": user,
        "enrollments": enrollments,
        "form": form,
    }
    return render(request, "students/profile.html", context)