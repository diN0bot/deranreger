from django.conf.urls.defaults import patterns, include, url
from deranreger.api.views import DataView

urlpatterns = patterns('',
    url(r'^data', DataView.as_view(), name='data'),
    #url(r'^event$', 'event'),
    #url(r'^events$', 'events'),
    #rl(r'^delete$', 'delete'),
)
