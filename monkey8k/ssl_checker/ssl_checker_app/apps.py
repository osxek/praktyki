from django.apps import AppConfig


class SslCheckerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ssl_checker_app'

def ready(self):
        import ssl_checker_app.signals