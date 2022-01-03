from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class LoginTemplateView(TemplateView):
    template_name = 'login_signup/login.html'


class SingnupTemplateView(TemplateView):
    template_name = 'login_signup/signup.html'
