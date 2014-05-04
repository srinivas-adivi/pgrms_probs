"""
URLs for the cars app.
"""
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'cars.views.cars_view', name='cars'),
    url(r'(?P<pk>[0-9]+)/$', 'cars.views.car_details', name='cars'),
)
