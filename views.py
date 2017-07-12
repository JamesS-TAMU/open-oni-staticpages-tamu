import os
import re
import warnings

from django.shortcuts import render
from django import template
from django.http import Http404, HttpResponse

# Prefix and Suffix define constant strings we use when rendering any static page
Prefix = "{% extends '__l_main.html' %}{% load static from staticfiles %}{% block content %}<div id=\"std_box\">"
Suffix = "</div><!-- end id:std_box -->\n{% endblock %}"

def page(request, pagename):
    # This makes sure we don't have stupid characters in the page name
    m = re.search('[^\w_-]', pagename)
    if m != None:
        warnings.warn("Attempt to render invalid pagename %s" % pagename)
        raise Http404

    # We allow subdirectories via a magic double-underscore
    pagename = re.sub('__', '/', pagename)

    # Check for the existence of, and then read, the requested template
    pagespath = os.path.dirname(os.path.abspath(__file__))
    pagefile = os.path.join(pagespath, "pages", pagename + ".html")
    if not os.path.exists(pagefile):
        warnings.warn("Attempt to render nonexistent page %s (file: %s)" % (pagename, pagefile))
        raise Http404

    text = open(pagefile, "r").read()
    tmpl = template.Template(Prefix + text + Suffix)
    c = template.RequestContext(request, {})
    return HttpResponse(tmpl.render(c))
