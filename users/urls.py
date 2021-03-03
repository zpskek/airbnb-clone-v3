from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("login/github/", views.github_login, name="github-login"),
    path(
        "login/github/callback/",
        views.github_login_callback,
        name="github-callback",
    ),
    path("login/kakao/", views.kakao_login, name="kakao-login"),
    path(
        "login/kakao/callback/",
        views.kakao_login_callback,
        name="kakao-callback",
    ),
    path("logout/", views.log_out, name="logout"),
]
