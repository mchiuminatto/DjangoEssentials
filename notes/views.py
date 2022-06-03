from django.shortcuts import render
from django.http import Http404

from .forms import NotesForm
from .models import Notes

# import to support class-based views (list views)
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic import DeleteView


# Create your views here.

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = "/smart/notes"

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = "/smart/notes"
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    success_url = "/smart/notes"
    form_class = NotesForm

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_view = "notes/notes_list.html"  # this is optional

class NoteDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_view = "notes/notes_detail.html"


