# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from homepage.models import Post
from django.http import HttpResponse


def index(request):
    first_post = Post.objects.first()
    return HttpResponse(
        "Hello, world. This is Cal's homepage. My first post is: {}".format(first_post.description)
    )
