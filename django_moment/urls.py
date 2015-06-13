from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from qrmecore.models import Box

urlpatterns = patterns('django_moment.views',
    url(r'(?P<counter_name>[a-z0-9_]+)/period.json', 'counter_period_json'),
    url(r'(?P<counter_name>[a-z0-9_]+)/', 'counter_dashboard'),
)

