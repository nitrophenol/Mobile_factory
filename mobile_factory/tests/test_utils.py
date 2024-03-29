from django.test import TestCase
from unittest.mock import patch
from mobile_factory.utils import startup_validations
from mobile_factory.enums import InputType, ComponentType, Component

class TestUtils(TestCase):

    @patch('mobile_factory.utils.COMPONENT_TYPE', {InputType.A: ComponentType.SCREEN})
    def test_startup_validations_component_type_sync(self):
        with self.assertRaises(AssertionError) as context:
            startup_validations()
        
        self.assertIn("COMPONENT_TYPE and InputType enums are not in sync", str(context.exception))


    @patch('mobile_factory.utils.COMPONENT_DATA', {InputType.A: Component.LED_SCREEN})
    def test_startup_validations_component_data_sync(self):
        with self.assertRaises(AssertionError) as context:
            startup_validations()
        
        self.assertIn("COMPONENT_DATA and InputType enums are not in sync", str(context.exception))
    
    @patch('mobile_factory.utils.PRICE_DATA', {InputType.A: 10.28})
    def test_startup_validations_price_data_sync(self):
        with self.assertRaises(AssertionError) as context:
            startup_validations()
        
        self.assertIn("PRICE_DATA and InputType enums are not in sync", str(context.exception))
    
    @patch('mobile_factory.utils.COMPONENT_TYPE', {InputType.A: ComponentType.SCREEN})
    def test_startup_validations_component_type_sync_again(self):
        with self.assertRaises(AssertionError) as context:
            startup_validations()
        
        self.assertIn("COMPONENT_TYPE and InputType enums are not in sync", str(context.exception))
    
    @patch('mobile_factory.utils.COMPONENT_DATA', {InputType.A: Component.LED_SCREEN})
    def test_startup_validations_component_data_sync_again(self):
        with self.assertRaises(AssertionError) as context:
            startup_validations()
        
        self.assertIn("COMPONENT_DATA and InputType enums are not in sync", str(context.exception))
