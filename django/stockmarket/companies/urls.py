"""
URLs for the stocks app.
"""
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'companies.views.companies_view', name='To view details of all companies group'),
    url(r'^(?P<code>[0-9]+)/(?P<startD>[0-9]{8})/(?P<endD>[0-9]{8})/$', 'companies.views.company_stock_details', name='Stock details for given company code in between given date range as in json'),
    url(r'(?P<code>[0-9]+)/(?P<startD>[0-9]{8})/$', 'companies.views.company_stock_details', name='Stock details of given company code on given day'),
    url(r'(?P<code>[0-9]+)/$', 'companies.views.company_details', name='Company details of given company code'),
)
