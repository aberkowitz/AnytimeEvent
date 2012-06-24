from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core import urlresolvers
from registration.forms import RegistrationForm
from registration.models import RegistrationProfile
from django.contrib.auth.decorators import login_required
from anytimeevent.models import Event 

from anytimeevent.models import EventDetails

def home(request):
    return render_to_response("home.html",
                              RequestContext(request))

def discover(request):
	event_list = Event.objects.all()
	return render_to_response("discover.html", event_list,
							  RequestContext(request))

@login_required
def user_events(request, number):
   try:
   	   p = User.objects.get(uid=number)
   except User.DoesNotExist:
   	   raise Http404
   events = Event.objects.filter(user=number)
   return render_to_response("user_events.html", 
   	                         RequestContext())

@login_required
def video(request, number):
   try:
       event = Event.objects.get(id=number)
   except Event.DoesNotExist:
       raise Http404
   return render_to_response("video.html",
                              {"event": event},
                              RequestContext(request))

@login_required
def addvideo(request, number):
   try:
       p = User.objects.get(uid=number)
   except User.DoesNotExist:
       raise Http404
   if request.method == 'POST':
       form = EventForm(request.POST)
       if form.is_valid():
           cd = form.cleaned_data
           cd.save()
   return render_to_response("addvideo.html",
							  RequestContext(request))
