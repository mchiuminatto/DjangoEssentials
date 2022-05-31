from django.shortcuts import render  
from django.http import HttpResponse  
from datetime import datetime

# authentication import 
from django.contrib.auth.decorators import login_required

# import to support class-based views
from django.views.generic import TemplateView

# mixin to support authetnication
from django.contrib.auth.mixins import LoginRequiredMixin
  
# Create your views here.  

class HomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {"today": datetime.today()}

# make sure LoginRequiredMixin is inherited before TemplateView
class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = "home/authorized.html"
    login_url = "/admin"