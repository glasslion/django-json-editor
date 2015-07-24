# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.forms import ModelForm

from djjsoneditor.widgets import JSONEditorWidget

from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'location': JSONEditorWidget()
        }

