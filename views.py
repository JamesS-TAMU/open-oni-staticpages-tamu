import os
import re
import warnings

from django.shortcuts import render
from django import template
from django.http import Http404, HttpResponse
from django.conf import settings

# Prefix and Suffix define constant strings we use when rendering any static page
Prefix = "{% extends '__l_main.html' %}{% load static from staticfiles %}{% block content %}<div id=\"std_box\">"
Suffix = "</div><!-- end id:std_box -->\n{% endblock %}"

def page(request, pagename):
    # We allow subdirectories via a magic double-underscore
    pagename = re.sub('__', '/', pagename)

    # Check for the existence of, and then read, the requested template
    if hasattr(settings, "STATIC_PAGES_PATH"):
        pagespath = settings.STATIC_PAGES_PATH
    else:
        pagespath = os.path.dirname(os.path.abspath(__file__))
        pagespath = os.path.join(pagespath, "pages")

    pagefile = os.path.join(pagespath, pagename + ".html")
    if not os.path.exists(pagefile):
        warnings.warn("Attempt to render nonexistent page %s (file: %s)" % (pagename, pagefile))
        raise Http404

    text = open(pagefile, "r").readlines()
    page_title = text[0]
    body = "\n".join(text[2:])

    tmpl = template.Template(Prefix + body + Suffix)
    c = template.RequestContext(request, {"page_title": page_title})
    return HttpResponse(tmpl.render(c))
