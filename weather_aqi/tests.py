# import json
# from django.test import TestCase, Client
# from django.urls import reverse
# from unittest.mock import patch
# from django.conf import settings
#
# class WeatherAPIViewTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#
#     @patch('requests.get')
#     def test_weather_api_view_success(self, mock_get):
#         mock_weather_response = {
#             'coord': {'lat': 51.51, 'lon': -0.13},
#             'main': {'temp': 20.0, 'humidity': 50},
#             'wind': {'speed': 5.0},
#             'weather': [{'description': 'clear sky'}],
#             'cod': 200
#         }
#         mock_air_pollution_response = {
#             'list': [{'main': {'aqi': 2}}]
#         }
#         mock_get.side_effect = [
#             MockResponse(status_code=200, json_data=mock_weather_response),
#             MockResponse(status_code=200, json_data=mock_air_pollution_response)
#         ]
#
#         response = self.client.get(reverse('api/weather', args=['London']))
#         self.assertEqual(response.status_code, 200)
#         data = json.loads(response.content.decode('utf-8'))
#         self.assertEqual(data['city'], 'London')
#         self.assertIn('weather', data)
#         self.assertIn('air_quality', data)
#         self.assertEqual(data['aqi_qualitative'], 'Fair')
#
#     @patch('requests.get')
#     def test_weather_api_view_weather_error(self, mock_get):
#         mock_weather_response = {
#             'cod': 404,
#             'message': 'City not found'
#         }
#         mock_get.return_value = MockResponse(status_code=404, json_data=mock_weather_response)
#
#         response = self.client.get(reverse('api/weather', args=['NonExistingCity']))
#         self.assertEqual(response.status_code, 400)
#         data = json.loads(response.content.decode('utf-8'))
#         self.assertEqual(data['error'], 'City not found')
#
#     @patch('requests.get')
#     def test_weather_api_view_air_pollution_error(self, mock_get):
#         mock_weather_response = {
#             'coord': {'lat': 51.51, 'lon': -0.13},
#             'main': {'temp': 20.0, 'humidity': 50},
#             'wind': {'speed': 5.0},
#             'weather': [{'description': 'clear sky'}],
#             'cod': 200
#         }
#         mock_air_pollution_response = {
#             'message': 'No data available for the requested location'
#         }
#         mock_get.side_effect = [
#             MockResponse(status_code=200, json_data=mock_weather_response),
#             MockResponse(status_code=404, json_data=mock_air_pollution_response)
#         ]
#
#         response = self.client.get(reverse('api/weather', args=['London']))
#         self.assertEqual(response.status_code, 400)
#         data = json.loads(response.content.decode('utf-8'))
#         self.assertEqual(data['error'], 'Error fetching air pollution data')
#
# class MockResponse:
#     def __init__(self, status_code, json_data):
#         self.status_code = status_code
#         self.json_data = json_data
#
#     def json(self):
#         return self.json_data
