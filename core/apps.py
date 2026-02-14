from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'
    from django.apps import AppConfig

    class Samplep1Config(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'Sample P1'

from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        import core.signals
class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        import core.signals
from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        import core.signals
def ready(self):
    import core.signals
