"""
Tests for the cars app.
"""
from django.test import TestCase
import mock
import json
from cars.models import Car
from cars.views import cars_view, car_details
from cars.forms import CarForm


class TestCar(TestCase):
    """Tests for the Car model."""
    def test_car(self):
        """Test the Car model."""
        car = Car()
        car.make = 'Make'
        car.model = 'Model'
        car.year = 1999

        car.save()


class TestCarForm(TestCase):
    """Tests for the car form."""
    def test_form(self):
        """Test that the form is attached to the right model."""
        self.assertIs(CarForm._meta.model, Car, 'Should be attached to Car.')


class TestIndexView(TestCase):
    """Tests for the cars.cars_view view."""
    @mock.patch('cars.views.CarForm')
    def test_post(self, MockCarForm):
        """Test a POST request to the cars_view view."""
        obj = {'make': 'Toyota', 'model': 'Camry', 'year': 2001}
        request = mock.Mock(
            method='POST',
            body=json.dumps(obj)
        )
        mock_form = MockCarForm.return_value
        mock_car = mock_form.save.return_value
        mock_car.id = 123

        response = cars_view(request)

        self.assertEqual(response.status_code, 201,
                         'Should return 201 CREATED.')
        self.assertEqual(response['Location'], '/cars/123',
                         'Should return the location of the new car.')
        MockCarForm.assert_called_with(obj)
        self.assertTrue(mock_form.save.called, 'Should call save.')

    def test_post_invalid_data(self):
        """Test POSTing invalid data."""
        request = mock.Mock(
            method='POST',
            body='{}'
        )

        response = cars_view(request)

        self.assertEqual(response.status_code, 400,
                         'Should return a 400 BAD REQUEST.')

    def test_post_bad_json(self):
        """Test POSTing invalid JSON."""
        request = mock.Mock(
            method='POST',
            body='fart'
        )

        response = cars_view(request)

        self.assertEqual(response.status_code, 400,
                         'Should return a 400 BAD REQUEST.')

    @mock.patch('cars.views.Car')
    def test_get(self, MockCar):
        """Test GET requests to the cars_view view."""
        request = mock.Mock(method='GET')
        objs = [
            {'id': 1, 'make': 'Make1', 'model': 'Model1', 'year': 1},
            {'id': 2, 'make': 'Make2', 'model': 'Model2', 'year': 2},
            {'id': 3, 'make': 'Make3', 'model': 'Model3', 'year': 3},
        ]
        MockCar.objects.all.return_value = [Car(**obj) for obj in objs]

        response = cars_view(request)
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200,
                         'Should return a successful response.')
        self.assertEqual(response['Content-Type'], 'application/json',
                         'Should return a JSON response.')
        self.assertSequenceEqual(data, objs, 'Should return the objects.')

    def test_not_supported(self):
        """Test sending an unsupported request method."""
        request = mock.Mock(method='FART')

        response = cars_view(request)

        self.assertEqual(response.status_code, 405,
                         'Should return a 405 NOT ALLOWED.')
        self.assertIn('GET', response['Allow'], 'Should allow GET.')
        self.assertIn('POST', response['Allow'], 'Should allow POST.')
    

class TestDetailsView(TestCase):
    """Tests for the cars.car_details view."""

    @mock.patch('cars.views.Car')
    def test_get(self, MockCar):
        """Test a GET request to the car_details view."""
        request = mock.Mock(method='GET')
        obj = {'id': 1, 'make': 'Make1', 'model': 'Model1', 'year': 1}
        
        MockCar.objects.get.return_value = Car(**obj)
        response = car_details(request, 1)
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200,
                         'Should return a successful response.')
        self.assertEqual(response['Content-Type'], 'application/json',
                         'Should return a JSON response.')
        self.assertDictEqual(data, obj, 'Should return the object.')
    
    @mock.patch('cars.views.Car')
    def test_put(self,  MockCar):
        """Test a PUT request to car_details view."""
        obj = {'make': 'Make1', 'model': 'Model1', 'year': 2013}
        request = mock.Mock(
            method='PUT',
            body=json.dumps(obj)
        )
        
        obj_in_db = {'id': 1, 'make': 'Make', 'model': 'Model', 'year': 2013}
        MockCar.objects.get.return_value = Car(**obj_in_db)
        response = car_details(request, 1)

        self.assertEqual(response.status_code, 205,
                         'Should return 205 CREATED.')
        self.assertEqual(response['Location'], '/cars/1',
                         'Should return the location of the new car.')
        self.assertIsNone(MockCar.objects.get.return_value.save(), 'Should call save.')
        
    @mock.patch('cars.views.Car')
    def test_delete(self, MockCar):
        """Test a DELETE request to the car_details view."""
        request = mock.Mock(method='DELETE')
        obj = {'id': 1, 'make': 'Make1', 'model': 'Model1', 'year': 1}
        response = car_details(request, 1)
        
        MockCar.objects.get.return_value = Car(**obj)
        
        self.assertEqual(response.status_code, 204,
                         'Should return 204 DELETE.')
        self.assertIsNone(MockCar.objects.get.return_value.delete(), 'Should call delete.')

    
    @mock.patch('cars.views.Car')
    def test_not_supported(self, MockCar):
        """Test sending an unsupported request method."""
        request = mock.Mock(method='FART')
        obj = {'id': 1, 'make': 'Make1', 'model': 'Model1', 'year': 1}
        response = car_details(request, 1)
        
        MockCar.objects.get.return_value = Car(**obj)

        response = car_details(request, 1)

        self.assertEqual(response.status_code, 405,
                         'Should return a 405 NOT ALLOWED.')
        self.assertIn('GET', response['Allow'], 'Should allow GET.')
        self.assertIn('DELETE', response['Allow'], 'Should allow DELETE.')
        self.assertIn('PUT', response['Allow'], 'Should allow PUT.')
