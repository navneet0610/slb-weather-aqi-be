import requests
from django.http import JsonResponse
from django.views import View
from django.conf import settings

class WeatherAPIView(View):
    def get(self, request, city_name):
        weather_api_key = settings.OPENWEATHERMAP_KEY

        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={weather_api_key}&units=metric"
        weather_response = requests.get(weather_url).json()
        if weather_response.get('cod') != 200:
            return JsonResponse({'error': weather_response.get('message', 'Error fetching weather data')}, status=400)

        lat, lon = weather_response['coord']['lat'], weather_response['coord']['lon']
        air_pollution_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={weather_api_key}"
        air_pollution_response = requests.get(air_pollution_url).json()

        aqi = air_pollution_response['list'][0]['main']['aqi']
        aqi_qualitative = {
            1: 'Good',
            2: 'Fair',
            3: 'Moderate',
            4: 'Poor',
            5: 'Very Poor'
        }.get(aqi, 'Unknown')

        data = {
            'city': city_name,
            'weather': weather_response,
            'air_quality': air_pollution_response,
            'aqi_qualitative': aqi_qualitative
        }

        return JsonResponse(data)
        # return {
        #     "city": "Delhi",
        #     "weather": {
        #         "coord": {
        #             "lon": 77.2167,
        #             "lat": 28.6667
        #         },
        #         "weather": [
        #             {
        #                 "id": 721,
        #                 "main": "Haze",
        #                 "description": "haze",
        #                 "icon": "50n"
        #             }
        #         ],
        #         "base": "stations",
        #         "main": {
        #             "temp": 28.95,
        #             "feels_like": 33.37,
        #             "temp_min": 28.95,
        #             "temp_max": 29.05,
        #             "pressure": 1001,
        #             "humidity": 74,
        #             "sea_level": 1001,
        #             "grnd_level": 976
        #         },
        #         "visibility": 4000,
        #         "wind": {
        #             "speed": 3.09,
        #             "deg": 100
        #         },
        #         "clouds": {
        #             "all": 40
        #         },
        #         "dt": 1720367368,
        #         "sys": {
        #             "type": 2,
        #             "id": 145989,
        #             "country": "IN",
        #             "sunrise": 1720310348,
        #             "sunset": 1720360356
        #         },
        #         "timezone": 19800,
        #         "id": 1273294,
        #         "name": "Delhi",
        #         "cod": 200
        #     },
        #     "air_quality": {
        #         "coord": {
        #             "lon": 77.2167,
        #             "lat": 28.6667
        #         },
        #         "list": [
        #             {
        #                 "main": {
        #                     "aqi": 5
        #                 },
        #                 "components": {
        #                     "co": 961.3,
        #                     "no": 0,
        #                     "no2": 14.4,
        #                     "o3": 117.3,
        #                     "so2": 23.84,
        #                     "pm2_5": 81.09,
        #                     "pm10": 96.26,
        #                     "nh3": 10.51
        #                 },
        #                 "dt": 1720367332
        #             }
        #         ]
        #     },
        #     "aqi_qualitative": "Very Poor"
        # }
