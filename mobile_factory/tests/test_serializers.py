from django.test import TestCase
from mobile_factory.serializers import CreateOrderSerializer


class TestCreateOrderSerializer(TestCase):
    def test_valid_data(self):
        # Test valid data
        data = {'components': ['I', 'A', 'D', 'F', 'K']}
        serializer = CreateOrderSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['components'], data['components'])
    
    def test_invalid_duplicate_components(self):
        # Test invalid data with duplicate components
        data = {'components': ['I', 'A', 'D', 'F', 'F']}
        serializer = CreateOrderSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(str(serializer.errors['non_field_errors'][0]), "Duplicate components are not allowed")

    def test_invalid_wrong_number_of_components(self):
        # Test invalid data with wrong number of components
        data = {'components': ['I', 'A', 'D', 'F']}
        serializer = CreateOrderSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(str(serializer.errors['non_field_errors'][0]), "Number of components in components list is not correct")
    def test_invalid_missing_components(self):
        # Test invalid data with missing components
        data = {}
        serializer = CreateOrderSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(str(serializer.errors['components'][0]), "This field is required.")
    def test_invalid_choices(self):
        # Test invalid JSON data
        data = {'components': ['Z','A','X']}
        serializer = CreateOrderSerializer(data=data )
        self.assertFalse(serializer.is_valid())
        self.assertEqual(str(serializer.errors['components'][0][0]), '"Z" is not a valid choice.')    
        self.assertEqual(str(serializer.errors['components'][2][0]), '"X" is not a valid choice.')
        