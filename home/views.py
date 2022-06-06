from django.shortcuts import render  
from django.http import HttpResponse  
from datetime import datetime
from django.shortcuts import redirect

# authentication import 
from django.contrib.auth.decorators import login_required

# import to support class-based views
from django.views.generic import TemplateView

# mixin to support authetnication
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView, LogoutView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
  
# Create your views here.  

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "home/register.html"
    success_url = "/smart/notes"

    # overrides CreateView get method to
    # redirect to user notes if logged in user is trying 
    # to sign up
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("notes.list")
        return super().get(request, *args, **kwargs)


class LoginInterfaceView(LoginView):
    template_name = "home/login.html"


class LogoutInterfaceView(LogoutView):
    template_name = "home/logout.html"

class HomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {"today": datetime.today()}
