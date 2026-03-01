from django.urls import path
from . import views
app_name = "students"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile/",views.student_profile,name="student_profile"),
]