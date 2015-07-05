from django.conf import settings
from django.http import HttpResponse
from django.conf.urls import include, patterns, url

from django_moment.models import Counter, Event

from .sites import MomentSite

debug_counter = Counter('debug_counter')
started_counter = Counter('started_counter')

debug_site = MomentSite()
debug_site.register(debug_counter)
debug_site.register(started_counter)

started_counter.inc()

def inc_debug_counter(request):
    debug_counter.inc()
    return HttpResponse("counter increased: %d" % debug_counter.get())

urlpatterns = debug_site.urls()
urlpatterns += patterns('django_moment.views',
    url(r'^inc/', inc_debug_counter),
)
