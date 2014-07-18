"""
URLs for the stocks app.
"""
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'companies.views.company_details', name='stock details of given company code'),
    url(r'(?P<startD>[0-9]{8})/(?P<endD>[0-9]{8})/$', 'companies.views.company_stock_details', name='stock details of given company code on given range'),
    url(r'(?P<startD>[0-9]{8})/$', 'companies.views.company_stock_details', name='stock details of given company code on given day'),
)
