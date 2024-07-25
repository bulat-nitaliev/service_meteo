from meteo import views
from django.urls import path
from rest_framework.routers import SimpleRouter
from meteo.views import UserViewSet


router = SimpleRouter()

router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('meteo/', views.MeteoViewSet.as_view()),
    path('city', views.CityViewSet.as_view()),
]

urlpatterns += router.urls