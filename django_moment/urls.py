from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView

from qrmecore.models import Box

urlpatterns = patterns('django_moment.views',
    url(r'^event/(?P<event_name>[\.a-zA-Z0-9_]+)/(?P<obj_name>[\.a-zA-Z0-9_]+)/period.json', 'event_period_json'),
    url(r'^event/(?P<event_name>[\.a-zA-Z0-9_]+)/(?P<obj_name>[\.a-zA-Z0-9_]+)/', 'event_dashboard'),
    url(r'^counter/(?P<counter_name>[\.a-zA-Z0-9_]+)/period.json', 'counter_period_json'),
    url(r'^counter/(?P<counter_name>[\.a-zA-Z0-9_]+)/', 'counter_dashboard'),
)
