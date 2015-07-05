from django.conf.urls import url

from django_moment.urls import urlpatterns

from .models import Counter, Event
from .views import SummaryView


class MomentSite (object):
    def __init__(self):
        self.counters = {}
        self.events = {}

    def register_counter(self, counter):
        self.counters[counter.name] = counter

    def register_event(self, event):
        self.events[event.name] = event

    def register(self, counter_or_event):
        if isinstance(counter_or_event, Counter):
            self.register_counter(counter_or_event)
        elif isinstance(counter_or_event, Event):
            self.register_event(counter_or_event)
        else:
            raise ValueError("Please give either a django_moment.models." + \
                    "Counter or django_moment.models.Event as the first " + \
                    "argument to this function.")

    def urls(self):
        return urlpatterns + [
                url(r'^$', SummaryView.as_view(site=self)),
            ]
