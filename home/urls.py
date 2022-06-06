from django.urls import path
from . import views

urlpatterns = [
path(r"", views.HomeView.as_view(), name="home"),
path(r"login", views.LoginInterfaceView.as_view(), name="login" ),
path(r"logout", views.LogoutInterfaceView.as_view(), name="logout" ),
path(r"signup", views.SignUpView.as_view(), name="signup" )
]

