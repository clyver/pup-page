# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Post(models.Model):

    """
    A singular piece of content.
    """

    description = models.CharField(max_length=1024, null=True, blank=True)
