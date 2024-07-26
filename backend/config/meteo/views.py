from django.shortcuts import render
from rest_framework.views import APIView
import requests
# import openmeteo_requests
# import pandas as pd
# import requests_cache
# from retry_requests import retry
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from meteo.serializers import CitySerializer, UserRegisterationSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from meteo.models import User, City
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework import status

class UserViewSet(CreateModelMixin,ListModelMixin,RetrieveModelMixin, GenericViewSet):
    # permission_classes = [IsAuthenticated]


    def get_serializer_class(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
            return UserRegisterationSerializer
        

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        return super().get_permissions()



class MeteoViewSet(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        longitude = request.GET.get('longitude')
        latitude = request.GET.get('latitude')
   
        url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}'
        params = '&current=temperature_2m,relative_humidity_2m,is_day,wind_speed_10m&daily=temperature_2m_max,temperature_2m_min,wind_speed_10m_max'
        res = requests.get(url+params)
        return Response({'res': dict(res.json())})


class CityViewSet(APIView):
    permission_classes = [IsAuthenticated]
    # queryset = City.objects.all()
    # serializer_class = CitySerializer
    def get(self, request, format=None):
        citys = City.objects.all()
        serializer = CitySerializer(citys, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # serializer = CitySerializer(data=request.data)
        res = request.data
        res['user'] = request.user.pk
        
        citys = City.objects.all().filter(name=res['name'])
        
        if not citys:
            res['count_city'] = 1 
            serializer = CitySerializer(data=res)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif citys: 
            print([i.count_city for i in citys])
            count = [i.count_city for i in citys][0] + 1
            # citys.count = count
            print(count)
            citys.update(count_city=count)
            # citys.save()
            return Response({'res': [(i.name,i.count_city) for i in citys]}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


    


