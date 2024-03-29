from django.apps import AppConfig
from mobile_factory.constants import COMPONENT_TYPE, COMPONENT_DATA, PRICE_DATA
from mobile_factory.enums import InputType, ComponentType, Component

class MobileFactory(AppConfig):

    name = 'mobile_factory'
    verbose_name = "Mobile Factory App"

    def ready(self):
        assert set([input_type.value for input_type in COMPONENT_TYPE]) == set([input_type.value for input_type in InputType]), "COMPONENT_TYPE and InputType enums are not in sync"
        assert set([input_type.value for input_type in COMPONENT_DATA]) == set([input_type.value for input_type in InputType]), "COMPONENT_DATA and InputType enums are not in sync"
        assert set([input_type.value for input_type in PRICE_DATA]) == set([input_type.value for input_type in InputType]), "PRICE_DATA and InputType enums are not in sync"

        assert set([COMPONENT_TYPE[input_type].name for input_type in COMPONENT_TYPE]) == set([component_type.name for component_type in ComponentType]), "COMPONENT_TYPE and ComponentType enums are not in sync"
        assert set([COMPONENT_DATA[input_type].name for input_type in COMPONENT_DATA]) == set([component.name for component in Component]), "COMPONENT_DATA and Component enums are not in sync"


        pass # startup code here