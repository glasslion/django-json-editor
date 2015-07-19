# -*- coding: utf-8 -*-
from django.db import models
from jsonfield import JSONField

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    location = JSONField()

