from django.contrib import admin
from django.db import models
from django import forms
from ckeditor.widgets import CKEditorWidget
from landingpage.models import LandingPageForm, LandingPage, Pitch

class PitchAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.CharField: {'widget': forms.Textarea},
        models.TextField: {'widget': CKEditorWidget}
    }

admin.site.register(LandingPageForm)
admin.site.register(LandingPage)
admin.site.register(Pitch, PitchAdmin)
