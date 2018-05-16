from django.apps import AppConfig


class ArbitrageConfig(AppConfig):
    name = 'arbitrage'
    def ready(self):
        print ('startup')
        pass