# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.shortcuts import render
from .forms import ContactForm

def demo_home(request):
    form = ContactForm()
    context = {}
    context['form'] = form
    return render(request, 'home.html', context)
