from dataclasses import asdict
from mobile_factory.controller.create_order_controller import CreateOrderController
from mobile_factory.errors import FailedToCreateOrder
import json
from rest_framework.decorators import api_view
from mobile_factory.serializers import CreateOrderSerializer
from mobile_factory.data_classes import Components
from rest_framework import response
# Your existing code for PRICE_DATA, COMPONENT_DATA, and REQUIRED_PARTS
from pdb import set_trace

@api_view(['POST'])
def create_order(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body.decode('utf-8'))
            order_serializer = CreateOrderSerializer(data=data)
            order_serializer.is_valid(raise_exception=True)
            input_order_data = order_serializer.validated_data
            components = Components(components=input_order_data.get('components'))
            create_order_controller = CreateOrderController(components)
            order = create_order_controller.create_order()
            return response.Response(asdict(order))
        except FailedToCreateOrder as e:
            return response.Response({"error": str(e)}, status=400)
        except json.JSONDecodeError:
            return response.Response({"error": "Invalid JSON data"}, status=400)
    return response.Response({"detail": "Method \"GET\" not allowed."}, status=405)
