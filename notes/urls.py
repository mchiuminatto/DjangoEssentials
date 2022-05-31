from django.urls import path

from . import views

urlpatterns = [
    path("notes", views.NotesListView.as_view(), name="notes"),
    path("notes/<int:pk>", views.NoteDetailView.as_view())
]