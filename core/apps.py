from django.apps import AppConfig
import signal


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self) -> None:
        import core.signals.handlers
