from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core import urlresolvers
from django.contrib.auth.decorators import login_required

from anytimeevent.models import EventDetails

def home(request):
    return render_to_response("home.html",
                              RequestContext(request))

@login_required
def video(request, number):
    eventDetails = EventDetails.objects.filter(id=number)

    return render_to_response("video.html",
                              {'number': number, 'eventDetails': eventDetails},
                              context_instance=RequestContext(request))
