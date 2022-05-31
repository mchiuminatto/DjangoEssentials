from django.shortcuts import render
from django.http import Http404

from .models import Notes

# import to support class-based views (list views)
from django.views.generic import DetailView, ListView


# Create your views here.

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_view = "notes/notes_list.html"  # this is optional

class NoteDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    # template_view = "notes/note_detail.html"


