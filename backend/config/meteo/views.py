from django.shortcuts import render
from rest_framework.views import APIView
import requests
# import openmeteo_requests
# import pandas as pd
# import requests_cache
# from retry_requests import retry
from rest_framework.response import Response
from meteo.serializers import CitySerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from meteo.models import User, City


class MeteoViewSet(APIView):
    def get(self, request):
        longitude = request.GET.get('longitude')
        latitude = request.GET.get('latitude')
   
        url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}'
        params = '&current=temperature_2m,relative_humidity_2m,is_day,wind_speed_10m&daily=temperature_2m_max,temperature_2m_min,wind_speed_10m_max'
        res = requests.get(url+params)
        return Response({'res': dict(res.json())})


class CityViewSet(ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    


