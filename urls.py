from django.conf.urls.defaults import *
from django.conf import settings
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import os
def php2html(request, path, page):
	return render_to_response(os.path.join(settings.MEDIA_ROOT, path) + '\\%s.php' % page)

def upload(request):
	if request.method == 'POST':
		if request.FILES:
			return HttpResponse()
	raise Http404

urlpatterns = patterns('django.views',
	(r'^admin/(.*)', admin.site.root),
	(r'^media/(?P<path>.+)$', 'static.serve', {'document_root': settings.MEDIA_ROOT +'/media'}),
	(r'^.+/upload.php', upload),
	(r'^(?P<path>.+)/(?P<page>.+).php', php2html),
	(r'^(?P<path>.+)$', 'static.serve', {'document_root': settings.MEDIA_ROOT +'/demos'}),
	(r'^$', 'generic.simple.direct_to_template', {'template': 'index.htm'}),
)
