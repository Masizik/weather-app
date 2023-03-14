import urllib.request

from django.shortcuts import render
from django.views import generic as views
from urllib.request import requests
import json


# Create your views here.
class IndexView(views.DetailView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        source_current = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=720dfb1dcf0e39692ddd35603283c28a').read()
        source_weekly = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/forecast?q=' + city + '&units=metric&appid=720dfb1dcf0e39692ddd35603283c28a').read()
        source_map = urllib.request.urlopen('https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png?appid=720dfb1dcf0e39692ddd35603283c28a').read()

        data_current = json.loads(source_current)
        data_weekly = json.loads(source_weekly)
        data_map = json.loads(source_map)

        context = super().get_context_data(**kwargs)
        context['country_code'] = str(data_current['sys']['country'])
        context['temperature'] = str(data_current['main']['temp']) + ' ℃'
        context['pressure'] = str(data_current['main']['pressure'])
        context['humidity'] = str(data_current['main']['humidity'])
        context['description'] = str(data_current['weather'][0]['description'])
        context['icon'] = str(data_current['weather'][0]['icon'])

        context['map'] = data_map

        context['temperature_weekly_first_day'] = str(data_weekly['list'][0]['main']['temp']) + ' ℃'
        context['pressure_weekly_first_day'] = str(data_weekly['list'][0]['main']['pressure'])
        context['humidity_weekly_first_day'] = str(data_weekly['list'][0]['main']['humidity'])
        context['description_weekly_first_day'] = str(data_weekly['list'][0]['weather'][0]['description'])
        context['icon_weekly_first_day'] = str(data_weekly['list'][0]['weather'][0]['icon'])

        context['temperature_weekly_second_day'] = str(data_weekly['list'][1]['main']['temp']) + ' ℃'
        context['pressure_weekly_second_day'] = str(data_weekly['list'][1]['main']['pressure'])
        context['humidity_weekly_second_day'] = str(data_weekly['list'][1]['main']['humidity'])
        context['description_weekly_second_day'] = str(data_weekly['list'][1]['weather'][0]['description'])
        context['icon_weekly_second_day'] = str(data_weekly['list'][1]['weather'][0]['icon'])

        context['temperature_weekly_third_day'] = str(data_weekly['list'][2]['main']['temp']) + ' ℃'
        context['pressure_weekly_third_day'] = str(data_weekly['list'][2]['main']['pressure'])
        context['humidity_weekly_third_day'] = str(data_weekly['list'][2]['main']['humidity'])
        context['description_weekly_third_day'] = str(data_weekly['list'][2]['weather'][0]['description'])
        context['icon_weekly_third_day'] = str(data_weekly['list'][2]['weather'][0]['icon'])

        context['temperature_weekly_fourth_day'] = str(data_weekly['list'][3]['main']['temp']) + ' ℃'
        context['pressure_weekly_fourth_day'] = str(data_weekly['list'][3]['main']['pressure'])
        context['humidity_weekly_fourth_day'] = str(data_weekly['list'][3]['main']['humidity'])
        context['description_weekly_fourth_day'] = str(data_weekly['list'][3]['weather'][0]['description'])
        context['icon_weekly_fourth_day'] = str(data_weekly['list'][3]['weather'][0]['icon'])

        context['temperature_weekly_fifth_day'] = str(data_weekly['list'][4]['main']['temp']) + ' ℃'
        context['pressure_weekly_fifth_day'] = str(data_weekly['list'][4]['main']['pressure'])
        context['humidity_weekly_fifth_day'] = str(data_weekly['list'][4]['main']['humidity'])
        context['description_weekly_fifth_day'] = str(data_weekly['list'][4]['weather'][0]['description'])
        context['icon_weekly_fifth_day'] = str(data_weekly['list'][4]['weather'][0]['icon'])






