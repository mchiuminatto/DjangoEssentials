from django.urls import path

from . import views

urlpatterns = [
    path("notes", views.list, name="notes"),
    path("notes/<int:pk>", views.detail, name="Notes detail")
]