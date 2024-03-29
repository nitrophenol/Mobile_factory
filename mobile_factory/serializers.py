from rest_framework import serializers
from mobile_factory.enums import InputType, ComponentType, Component
from mobile_factory.constants import COMPONENT_TYPE

class CreateOrderSerializer(serializers.Serializer):
    components = serializers.ListField(child=serializers.ChoiceField(choices=(InputType.get_values())))

    def validate(self, attrs):
        if len(attrs['components']) != len(ComponentType.get_keys()):
            raise serializers.ValidationError("Number of components in components list is not correct")
        if set([COMPONENT_TYPE[InputType[components]].name for components in attrs['components']]) != set(ComponentType.get_keys()):
            raise  serializers.ValidationError("Duplicate components are not allowed")
        return super().validate(attrs)