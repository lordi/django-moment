from django.apps import AppConfig
from moment import conf

class MomentConfig(AppConfig):
    name = 'django_moment'
    verbose_name = "Moment"

    def ready(self):
        # Register default connection 
        conf.register_connection()

        # Register some other connection
        conf.register_connection(alias='analytics', host='localhost', port=6379)

        self.conn = conf.get_connection('analytics')
