from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter email address"
        })
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Choose a username"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Style password fields
        self.fields["password1"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Create password"
        })

        self.fields["password2"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Confirm password"
        })

    def save(self, commit=True):
        user = super().save(commit=False)

        # FORCE student role
        user.is_student = True
        user.is_teacher = False
        user.is_parent = False

        if commit:
            user.save()

        return user


class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
        widgets = {
            "image": forms.ClearableFileInput(attrs={
                "class": "form-control"
            })
        }
