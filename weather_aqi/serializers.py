from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    city = serializers.CharField()
    weather = serializers.JSONField()
    air_quality = serializers.JSONField()
    aqi_qualitative = serializers.CharField()
