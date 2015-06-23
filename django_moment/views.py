from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from moment import (COUNTER_ALIASES, EVENT_ALIASES, DayCounter, MonthCounter,
                    WeekCounter, YearCounter)

from .models import Counter, Event

dashboard_counter = Counter('dashboard')
dashboard_update_counter = Counter('dashboard_update')
dashboard_event = Event('dashboardev', 'languages')

def counter_period_json(request, counter_name):
    dashboard_update_counter.inc()
    response_dict = {}
    for (key, cls) in COUNTER_ALIASES.iteritems():
        counter = cls.from_date(counter_name)
        items = []
        for i in range(10):
            items.append(dict(counter.items(),
                            period_start=counter.period_start(),
                            period_end=counter.period_end()))
            counter = counter.delta(-1)
        response_dict[key] = items
    return JsonResponse(response_dict)

def event_period_json(request, event_name, obj_name):
    dashboard_event.record(request.META['SERVER_NAME'])
    response_dict = {}
    for (key, cls) in EVENT_ALIASES.iteritems():
        event = cls.from_date(event_name, sequence='languages')
        items = []
        for i in range(10):
            items.append(dict({obj_name: event.is_recorded(obj_name)},
                            period_start=event.period_start(),
                            period_end=event.period_end()))
            event = event.delta(-1)
            event.sequence = 'languages'
        response_dict[key] = items
    return JsonResponse(response_dict)

def counter_dashboard(request, counter_name):
    dashboard_counter.inc()
    return render(request, 'django_moment/counter_dashboard.html', {
        'counter': counter_name
    })

def event_dashboard(request, event_name, obj_name):
    dashboard_event.record(request.META['SERVER_NAME'])
    print request.META['SERVER_NAME']
    period_json_url = reverse(event_period_json, kwargs=dict(event_name=event_name, obj_name=obj_name))
    return render(request, 'django_moment/event_dashboard.html', {
        'event': event_name,
        'obj_name': obj_name,
        'period_json_url': period_json_url
    })

class SummaryView(TemplateView):
    template_name = 'django_moment/summary.html'
    site = None

    def get_context_data(self, **kwargs):
        context = super(SummaryView, self).get_context_data(**kwargs)
        context['counters'] = self.site.counters
        context['events'] = self.site.events
        return context

class CounterDashboardView(TemplateView):
    template_name = 'django_moment/counter_dashboard.html'
    site = None

    def get_context_data(self, **kwargs):
        dashboard_counter.inc()
        context = super(CounterDashboardView, self).get_context_data(**kwargs)
        context['counter'] = kwargs.get('counter_name')
        return context

