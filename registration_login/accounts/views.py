from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'login.html'

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
