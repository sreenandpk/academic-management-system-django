# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup_view, role_login_redirect_view

app_name = "accounts"

urlpatterns = [
    path("signup/", signup_view, name="signup"),
      # ✅ redirect_authenticated_user=True → logged-in users cannot see login page
    path(
        "",
        auth_views.LoginView.as_view(
            template_name="accounts/login.html",
            redirect_authenticated_user=True
        ),
        name="login"
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="accounts:login"), name="logout"),

    # this redirects after login
    path("profile-redirect/", role_login_redirect_view, name="profile-redirect"),

]
