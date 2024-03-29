from django.apps import AppConfig
from mobile_factory.utils import startup_validations

class MobileFactory(AppConfig):

    name = 'mobile_factory'
    verbose_name = "Mobile Factory App"

    def ready(self):
        startup_validations()
        pass # startup code here