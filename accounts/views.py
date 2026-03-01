# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("accounts:profile-redirect")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": form})

def role_login_redirect_view(request):
    # protect anonymous users
    if not request.user.is_authenticated:
        return redirect("accounts:login")

    user = request.user

    if user.is_superuser or user.is_staff:
        return redirect('/admin/')

    # Use literal URL paths as a temporary fallback (won't raise NoReverseMatch)
    if getattr(user, "is_teacher", False):
        return redirect('/teachers/dashboard/')   # <-- temporary safe fallback

    if getattr(user, "is_parent", False):
        return redirect('/parents/dashboard/')

    if getattr(user, "is_student", False):
        return redirect('/students/dashboard/')

    return redirect('/')


