from django.apps import AppConfig


class MecanicoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mecanico'

    def ready(self):
        import mecanico.signals
