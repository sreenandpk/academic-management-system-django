from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Admin panel settings for custom User model with student management."""

    inlines = (ProfileInline,)

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_student",
        "is_teacher",
        "is_parent",
        "is_staff",
        "is_active",
        "is_superuser",
    )

    list_filter = (
        "is_student",
        "is_teacher",
        "is_parent",
        "is_staff",
        "is_superuser",
        "is_active",
    )

    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("username",)

    fieldsets = UserAdmin.fieldsets + (
        (_("Roles"), {"fields": ("is_student", "is_teacher", "is_parent")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username",
                "email",
                "password1",
                "password2",
                "is_student",
                "is_teacher",
                "is_parent",
            ),
        }),
    )

    list_editable = ("is_student", "is_teacher", "is_parent")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "image")
