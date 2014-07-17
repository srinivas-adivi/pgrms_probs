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
    url(r'^goc/$', 'companies.views.companies_view', name='home'),
    url(r'^goc[a-zA-Z_]*/stocks/', include('stocks.urls')),
    url(r'^goc[a-zA-Z_]*/(?P<code>[0-9]+)/', include('companies.urls')),
)
