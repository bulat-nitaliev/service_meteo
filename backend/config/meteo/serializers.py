from rest_framework import serializers
from meteo.models import User, City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        models = City
        fields = '__all__'