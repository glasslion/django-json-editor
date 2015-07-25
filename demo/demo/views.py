# -*- coding: utf-8 -*-
from __future__ import absolute_import
import json

from django.shortcuts import render
from .forms import ContactForm

def demo_home(request):
    location_example = {
        "address" : ["126 york street", "second and third floor"],
        "zip" : "k1n5t5",
        "city" : "ottawa",
        "province" : "ontario",
        "country" : "CA",
    }
    form = ContactForm(initial={
        'location':json.dumps(location_example)
    })
    context = {}
    context['form'] = form
    return render(request, 'home.html', context)
