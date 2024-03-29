from django.test import TestCase
from mobile_factory.views import create_order
from rest_framework.test import APIClient

class TestCreateOrderView(TestCase):
    def setUp(self):
     self.client = APIClient()
    def test_create_order_view(self):
        # Test create order view
        response = self.client.post('/orders', {'components': ['I', 'A', 'D', 'F', 'K']}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['total'], 142.3)
        self.assertEqual(response.json()['parts'], ['Android OS', 'LED Screen', 'Wide-Angle Camera', 'USB-C Port', 'Metallic Body'])
        self.assertTrue(response.json()['order_id'])

    def test_create_order_view_invalid_duplicate_components(self):
        # Test create order view with duplicate components
        response = self.client.post('/orders', {'components': ['I', 'A', 'D', 'F', 'F']}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['non_field_errors'][0], "Duplicate components are not allowed")

    def test_create_order_view_invalid_wrong_number_of_components(self):
        # Test create order view with wrong number of components
        response = self.client.post('/orders', {'components': ['I', 'A', 'D', 'F']}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['non_field_errors'][0], "Number of components in components list is not correct")

    def test_create_order_view_invalid_missing_components(self):
        # Test create order view with missing components
        response = self.client.post('/orders', {} , format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['components'][0], "This field is required.")
    def test_create_order_view_invalid_json_data(self):
        # Test create order view with invalid JSON data
        response = self.client.post('/orders', 'invalid_json_data', content_type='text/plain')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], "Invalid JSON data")    
    def test_create_order_view_invalid_request_method(self):
        # Test create order view with invalid request method
        response = self.client.get('/orders')
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json()['detail'], 'Method "GET" not allowed.')    
    