from django.conf.urls import patterns, include, url
from blog.settings import DEBUG
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from main.models import *
from feed import theFeed

urlpatterns = patterns('',

    (r'^$', 'views.index'),
    (r'^admin/', include(admin.site.urls)),
    (r'^(\d{4})/(\d{1,2})/(\d{1,2})/([a-zA-Z0-9_-]+)/$', 'views.details'),
    (r'^category/([\w]+)/$', 'views.category'),
    (r'^feed/$', theFeed()),
    (r'^comments/', include('django.contrib.comments.urls')),  
)

if DEBUG:
    urlpatterns += patterns('', (
        r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'static'}))
