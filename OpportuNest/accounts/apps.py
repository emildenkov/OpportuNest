from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'OpportuNest.accounts'

    def ready(self):
        import OpportuNest.accounts.signals