from django.apps import AppConfig
from django.conf import settings

from moment import conf


class MomentConfig(AppConfig):
    name = 'django_moment'
    verbose_name = "Moment"

    defaults = {
        'DJANGO_MOMENT_REDIS_HOST': 'localhost',
        'DJANGO_MOMENT_REDIS_PORT': 6379
    }

    def _get_setting(self, setting):
        return getattr(settings, setting, self.defaults.get(setting))

    def ready(self):
        conf.register_connection(alias='default',
                host=self._get_setting('DJANGO_MOMENT_REDIS_HOST'),
                port=self._get_setting('DJANGO_MOMENT_REDIS_PORT'))
