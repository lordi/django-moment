from moment import update_counters, COUNTER_ALIASES

ALL_COUNTER_TYPES = COUNTER_ALIASES.keys()

class Counter():
    def __init__(self, name, ctypes=ALL_COUNTER_TYPES):
        self.name = name
        self.ctypes = ctypes

    def inc(self, amt=1):
        update_counters(self.name, {'count': amt}, counter_types=self.ctypes)

