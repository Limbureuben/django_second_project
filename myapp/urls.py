from django.urls import path
from project.myapp.views import current_weather, hourly_average_summary

urlpatterns = [
    path('api/hourly-average-summary/', hourly_average_summary, name='hourly_average_summary'),
    path('api/current-weather/', current_weather, name='current-weather'),
]