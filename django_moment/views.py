from django.http import JsonResponse
from django.shortcuts import render

from moment import (COUNTER_ALIASES, DayCounter, MonthCounter, WeekCounter,
                    YearCounter)
from .models import Counter

dashboard_counter = Counter('dashboard')

def counter_period_json(request, counter_name):
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

def counter_dashboard(request, counter_name):
    dashboard_counter.inc()
    return render(request, 'django_moment/dashboard.html', {
        'counter': counter_name
    })
