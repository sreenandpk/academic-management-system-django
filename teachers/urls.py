# teachers/urls.py
from django.urls import path
from . import views

app_name = "teachers"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile/", views.teacher_profile, name="teacher_profile"),   # ✅ new
    path("course/<int:course_id>/students/", views.course_students, name="course_students"),  # ✅ new
     path("<int:course_id>/materials/", views.teacher_course_materials, name="teacher_course_materials"),  # ✅ add this

]