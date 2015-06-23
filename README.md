# django-moment
Django real-time analytics powered by redis-moment

## Installation
TODO

## Features
1. Easy, scalable counters and events (see redis-moment)
2. Integrated analytics page

## How to use

### Quick start

Create a ``analytics.py`` in your project with all the events and counters:

```python
from django_moment.models import Counter, Event

visitors = Counter('visitors')
user_online_event = Event('user_online', sequence='users')
```

Everywhere you want to increase the counter or record the occurance of an event, do this:

```python
from myapp.analytics import visitors, user_online_event

visitors.inc()
user_online_event.record([user_id])
```

### Analytics page

Extend the ``analytics.py``:

```python
from django_moment.site import MomentSite

analytics_site = MomentSite()
analytics_site.register(visitors)
analytics_site.register(user_online_event)
```

In your ``urls.py``:

```python
from myapp.analytics import analytics_site

urlpatterns += patterns('',
    url(r'^analytics/', include(analytics_site.urls()))
)
```
