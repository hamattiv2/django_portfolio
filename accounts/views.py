from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model, login
from django.views.generic import CreateView, TemplateView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from . import forms

class LoginView(LoginView):
    template_name = "accounts/login.html"
    form_class = forms.LoginForm

class LogoutView(LogoutView):
    template_name = "accounts/logout.html"

class UserPage(LoginRequiredMixin, TemplateView):
    login_url = "/accounts/login"
    template_name = "accounts/userpage.html"
    model = get_user_model()
    context_object_name = "user"

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(get_user_model(), username=kwargs["username"])
        if user.id == self.request.user.id:
            return super().get(request, **kwargs)
        else:
            return render(self.request, "403.html")

class SignUp(CreateView):
    template_name = "accounts/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())
