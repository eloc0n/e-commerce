from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):            # connects signals with the app
        import accounts.signals 
