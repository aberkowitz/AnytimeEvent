from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/', include('social_auth.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', 'anytimeevent.views.home', name='home'),
    url(r'^video/(?P<number>\d{1,})', 'anytimeevent.views.video', name='video'),
    url(r'^addvideo', 'anytimeevent.views.addvideo', name='addVideo'),

    # url(r'^anytimeevent/', include('anytimeevent.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
