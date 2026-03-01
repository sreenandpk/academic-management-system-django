# materials/urls.py
from django.urls import path
from . import views

app_name = "materials"

urlpatterns = [
    # Student view: list materials for a course
    path("course/<int:course_id>/", views.course_materials, name="course_materials"),

    # Teacher view: upload new material to a course
    path("upload/<int:course_id>/", views.upload_material, name="upload_material"),
]