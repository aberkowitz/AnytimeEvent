from django.forms import ModelForm

class EventForm(ModelForm)
    class Meta:
    	model = Event
    	fields = ('slidesURI', 'videoURI', 'externalURI', 'price', 'eventName', 'eventDate', 'eventLocation', 'speakers', 'price', 'promoCode')
	#eventURLField = forms.URLField(label='Please enter the web address of your Eventbrite event', max_length=400)
	#videoURLField = forms.URLField(label='To submit a video, please enter a YouTube URL:', max_length=400)
	#slidesURLField = forms.URLField(label='To submit a slide presentation, please enter a Slideshare URL:', max_length=400)
	#eventNameField = forms.Charfield(label='Event Name:', max_length=200)
	#eventDateField = forms.DateTimeField(label='Date:')
	#eventLocationField = forms.CharField(label='Location:', widget=forms.Textarea)
	#eventSpeakers = forms.CharField(label='Speaker(s):', widget=forms.Textarea)
	#eventOnlinePrice = forms.DecimalField(label='Price for non-attendees:', max_digits=3, decimal_places=2)
	#eventPromoCode = forms.CharField(label='Promo code for attendees:', max_length=10)