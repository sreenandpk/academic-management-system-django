# enrollments/admin.py
from django.contrib import admin
from .models import Enrollment
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "get_subject", "date_joined")
    search_fields = ("student__username", "course__name", "course__subject__name")
    list_filter = ("course__subject", "date_joined")

    def get_subject(self, obj):
        return obj.course.subject.name
    get_subject.short_description = "Subject"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "student":
            kwargs["queryset"] = User.objects.filter(is_student=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)