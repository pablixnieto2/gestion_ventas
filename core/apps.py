from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = 'Gestión de Ventas'

    def ready(self):
        import core.signals  # Importa señales para la aplicación, si tienes alguna configurada