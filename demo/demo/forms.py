# -*- coding: utf-8 -*-
from __future__ import absolute_import
import json

from django.forms import ModelForm, ValidationError
from djjsoneditor.widgets import JSONEditorWidget

from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'location': JSONEditorWidget()
        }

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        location = cleaned_data.get("location")
