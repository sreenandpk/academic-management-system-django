from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.course_index, name="course_index"),  # all courses
    path("<int:subject_id>/", views.course_list_by_subject, name="course_list_by_subject"),
]