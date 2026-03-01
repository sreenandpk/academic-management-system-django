from django.contrib import admin
from .models import Course
from django.contrib.auth import get_user_model

User = get_user_model()

# Custom filter to show only teachers in the sidebar
class TeacherFilter(admin.SimpleListFilter):
    title = 'Teacher'
    parameter_name = 'teacher'

    def lookups(self, request, model_admin):
        teachers = User.objects.filter(is_teacher=True)
        return [(teacher.id, teacher.username) for teacher in teachers]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(teacher__id=self.value())

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Admin panel settings for Course model with teacher restriction."""

    # Columns displayed in admin course list
    list_display = ("name", "teacher", "get_subject", "created_at", "updated_at")

    # Filters on right side — use custom teacher filter
    list_filter = (TeacherFilter, "subject", "created_at")

    # Search bar fields
    search_fields = ("name", "description", "subject__name")

    # Default ordering
    ordering = ("subject__name", "name")

    # Restrict teacher dropdown to only users with is_teacher=True
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            kwargs["queryset"] = User.objects.filter(is_teacher=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_subject(self, obj):
        return obj.subject.name if obj.subject else "-"
    get_subject.short_description = "Subject"