from django.conf.urls.defaults import *

urlpatterns = patterns('',
  url(r'^(?P<library>\w+)/combo$', 'djamboloader.views.load', name='load'),
)
