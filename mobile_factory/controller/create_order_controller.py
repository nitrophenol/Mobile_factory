import json
from django.http import JsonResponse
from mobile_factory.constants import PRICE_DATA, COMPONENT_DATA
from mobile_factory.enums import InputType

from mobile_factory.data_classes import CreateOrderResponse
from uuid import uuid4
import pdb
class CreateOrderController:
    def __init__(self, components):
        self.components = components

    def create_order(self):
        return CreateOrderResponse(
            order_id=uuid4(),
            total=sum(PRICE_DATA[InputType[component]] for component in self.components.components),
            parts=[COMPONENT_DATA[InputType[component]].value for component in self.components.components]
        )

