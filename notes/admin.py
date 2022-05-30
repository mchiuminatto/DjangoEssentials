from django.contrib import admin

# import applicaiton models
from . import models

class NotesAdmin(admin.ModelAdmin):
    # no additional configuration required so far
    list_display = ("title", )


# model registration

admin.site.register(models.Notes, NotesAdmin)
