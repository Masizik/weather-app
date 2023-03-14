from django.urls import path

from WeatherApp.weather_app.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
