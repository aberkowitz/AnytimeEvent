from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
	slidesURI = models.URLField(blank=False, max_length=400, verbose_name='To submit a slide presentation, please enter a Slideshare URL:')
	videoURI  = models.URLField(blank=False, max_length=400, verbose_name='To submit a video, please enter a YouTube URL:')
	externalURI  = models.URLField(blank=False, max_length=400, verbose_name='Please enter the web address of your Eventbrite event:')
	price = models.DecimalField(blank=False, max_digits=3, decimal_places=2, verbose_name='Promo code for attendees:')
	promoCode = models.CharField(max_length=10, verbose_name='Price for non-attendees:')
	speakers = models.TextField(verbose_name='Speaker(s):');
	pubdate = models.DateTimeField('date published', auto_now=True)
	eventName = models.CharField(max_length=200, verbose_name='Event Name:')
	eventDate = models.DateTimeField(False, False)
	eventLocation = models.TextField(verbose_name='Location:')
	user = models.ForeignKey(User)
