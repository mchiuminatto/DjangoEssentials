from django.urls import path
from . import views

urlpatterns = [
path(r"home", views.HomeView.as_view(), name="home"),
path(r"authorized", views.AuthorizedView.as_view(), name="authorized" )
]

