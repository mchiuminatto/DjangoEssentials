from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from .forms import NotesForm
from .models import Notes

# import to support class-based views (list views)
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = "/smart/notes"

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = "/smart/notes"
    form_class = NotesForm

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = "/smart/notes"
    form_class = NotesForm
    login_url = "/admin"

    def form_valid(self, form):
        self.object = form.save(commit=False)  # validates the form but does not save it to the database
        self.object.user = self.request.user
        self.object.save()  # this time saves the object to the database
        return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_view = "notes/notes_list.html"  # this is optional
    login_url = "/admin"

    def get_queryset(self):
        return self.request.user.notes.all()
        

class NoteDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_view = "notes/notes_detail.html"


