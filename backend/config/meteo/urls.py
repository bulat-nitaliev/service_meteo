from meteo import views
from django.urls import path

urlpatterns = [
    path('meteo/', views.MeteoViewSet.as_view()),
    path('city/', views.CityViewSet.as_view({'get': 'list'})),
]