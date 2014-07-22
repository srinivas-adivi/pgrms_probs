"""
URLs for the stocks app.
"""
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'stocks.views.stocks_view', name='stock details of given company code'),
    url(r'^(?P<code>[0-9]+)/$', 'stocks.views.stock_details', name='stock details of given company code'),
)
