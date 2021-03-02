from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse


class LoginOnlyView(LoginRequiredMixin):
    login_url = reverse_lazy("users:login")


class LoggedOutOnlyView(UserPassesTestMixin):

    permission_denied_message = "Page Not Found"

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect(reverse("core:home"))
