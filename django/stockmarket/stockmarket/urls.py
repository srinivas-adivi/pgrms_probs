"""
URLs for the stockmarket project.
"""
from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stockmarket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^goc/', include('companies.urls')),
    url(r'^goc_range/(?P<code>[0-9]+)/(?P<startD>[0-9]{8})/(?P<endD>[0-9]{8})/$', 'companies.views.company_stocks_graph', name='Graphical output of stock details for given company code in between given date range'),
    url(r'^stocks/', include('stocks.urls')),
)
