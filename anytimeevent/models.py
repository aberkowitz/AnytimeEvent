from django.db import models

class Event(models.Model):
	slidesURI = models.URLField(blank=False, max_length=400)
	videoURI  = models.URLField(blank=False, max_length=400)
	externalURI  = models.URLField(blank=False, max_length=400)
	price = models.DecimalField(blank=False, max_digits=3, decimal_places=2)
	promoCode = models.CharField(max_length=10)
	pubdate = models.DateTimeField('date published', auto_now=True)
	user = models.ForeignKey(User)

class EventDetails(models.Model):
	event = models.ForeignKey(Event)
	eventName = models.CharField(max_length=200)
	eventDate = models.DateTimeField(False, False)
	eventLocation = models.TextField()