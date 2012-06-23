from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core import urlresolvers

def home(request):
    return render_to_response("home.html",
                              RequestContext(request))