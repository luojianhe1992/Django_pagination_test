from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Contact(models.Model):
    name = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    address = models.TextField(max_length=10000)