from django.core.urlresolvers import reverse

from moment import (COUNTER_ALIASES, EVENT_ALIASES, record_events,
                    update_counters)

ALL_COUNTER_TYPES = COUNTER_ALIASES.keys()
ALL_EVENT_TYPES = EVENT_ALIASES.keys()

class Counter(object):
    def __init__(self, name, ctypes=ALL_COUNTER_TYPES):
        self.name = name
        self.ctypes = ctypes

    def inc(self, amt=1):
        update_counters(self.name, {'count': amt}, counter_types=self.ctypes)

    def get(self, ctype='day'):
        cls = COUNTER_ALIASES.get(ctype)
        today = cls.from_date(self.name)
        return today.items()[0][1]

    def get_absolute_url(self):
        return reverse('django_moment.views.counter_dashboard',
                kwargs=dict(counter_name=self.name))


class Event(object):
    def __init__(self, name, sequence, ctypes=ALL_EVENT_TYPES):
        self.name = name
        self.sequence = sequence
        self.ctypes = ctypes

    def record(self, whom):
        record_events(whom, self.name, sequence=self.sequence)

    def get_absolute_url(self):
        return reverse('django_moment.views.event_dashboard',
                kwargs=dict(event_name=self.name))
