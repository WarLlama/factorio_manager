# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Container(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    image = models.CharField(max_length=255)
    created = models.DateTimeField()
    started = models.DateTimeField()
    status = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
