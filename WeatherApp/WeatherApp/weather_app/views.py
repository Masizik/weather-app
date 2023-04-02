import urllib.request

from django.shortcuts import render
from django.views import generic as views
# from urllib.request import requests
import json

from WeatherApp.weather_app.forms import CreateHistoryModel
from WeatherApp.weather_app.models import HistoryModel


# Create your views here.
class IndexView(views.TemplateView):
    template_name = 'index.html'
    form_class = CreateHistoryModel
    model = HistoryModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city = str(self.request.GET.get('city'))
        num = 40
        weekly_temp = []
        weekly_pressure = []
        weekly_humidity = []
        weekly_description = []
        weekly_temp_min = []
        weekly_temp_max = []
        weekly_temp_feels_like = []
        weekly_speed = []
        weekly_icon = []
        weekly_date = []

        source_current = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=720dfb1dcf0e39692ddd35603283c28a').read()
        source_weekly = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/forecast?q=' + city + '&units=metric&appid=720dfb1dcf0e39692ddd35603283c28a').read()
        # source_map = urllib.request.urlopen('https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png?appid=720dfb1dcf0e39692ddd35603283c28a').read()

        data_current = json.loads(source_current)
        data_weekly = json.loads(source_weekly)
        # data_map = json.loads(source_map)

        for i in range(0, num):
            weekly_temp.append(str(data_weekly['list'][i]['main']['temp']) + ' ℃')
            weekly_pressure.append(str(data_weekly['list'][i]['main']['pressure']))
            weekly_humidity.append(str(data_weekly['list'][i]['main']['humidity']))
            weekly_description.append(str(data_weekly['list'][i]['weather'][0]['description']))
            weekly_temp_min.append(str(data_weekly['list'][i]['main']['temp_min']) + ' ℃')
            weekly_temp_max.append(str(data_weekly['list'][i]['main']['temp_max']) + ' ℃')
            weekly_temp_feels_like.append(str(data_weekly['list'][i]['main']['feels_like']) + ' ℃')
            weekly_speed.append(str(data_weekly['list'][i]['wind']['speed']) + ' mph')
            weekly_icon.append(str(data_weekly['list'][i]['weather'][0]['icon']))
            weekly_date.append(str(data_weekly['list'][i]['dt_txt']))

        context['city'] = city
        context['num'] = range(0, len(weekly_temp))
        context['country_code'] = str(data_current['sys']['country'])
        context['temperature'] = str(data_current['main']['temp']) + ' ℃'
        context['pressure'] = str(data_current['main']['pressure'])
        context['humidity'] = str(data_current['main']['humidity'])
        context['description'] = str(data_current['weather'][0]['description'])
        context['temp_min'] = str(data_current['main']['temp_min']) + ' ℃'
        context['temp_max'] = str(data_current['main']['temp_max']) + ' ℃'
        context['feels_like'] = str(data_current['main']['feels_like']) + ' ℃'
        context['speed'] = str(data_current['wind']['speed']) + ' mph'
        context['icon'] = str(data_current['weather'][0]['icon'])

        context['weekly_temp'] = weekly_temp
        context['weekly_description'] = weekly_description
        context['weekly_temp_max'] = weekly_temp_max
        context['weekly_temp_min'] = weekly_temp_min
        context['weekly_temp_feels_like'] = weekly_temp_feels_like
        context['weekly_humidity'] = weekly_humidity
        context['weekly_date'] = weekly_date
        context['weekly_pressure'] = weekly_pressure
        context['weekly_speed'] = weekly_speed
        context['weekly_icon'] = weekly_icon

        # context['weekly_all'] = enumerate(zip(context['weekly_temp'], context['weekly_description']))

        context['weekly_all'] = dict(enumerate(zip(context['weekly_temp'], context['weekly_description'], context['weekly_temp_max'],context['weekly_temp_min'],context['weekly_temp_feels_like'],context['weekly_humidity'],context['weekly_date'],context['weekly_pressure'],context['weekly_speed'],context['weekly_icon'])))

        # context['map'] = data_map

        # context['temperature_weekly_first_day'] = str(data_weekly['list'][0]['main']['temp']) + ' ℃'
        # context['pressure_weekly_first_day'] = str(data_weekly['list'][0]['main']['pressure'])
        # context['humidity_weekly_first_day'] = str(data_weekly['list'][0]['main']['humidity'])
        # context['temp_min_weekly_first_day'] = str(data_weekly['list'][0]['main']['temp_min']) + ' ℃'
        # context['temp_max_weekly_first_day'] = str(data_weekly['list'][0]['main']['temp_max']) + ' ℃'
        # context['feels_like_weekly_first_day'] = str(data_weekly['list'][0]['main']['feels_like']) + ' ℃'
        # context['speed_weekly_first_day'] = str(data_weekly['list'][0]['wind']['speed']) + ' mph'
        # context['description_weekly_first_day'] = str(data_weekly['list'][0]['weather'][0]['description'])
        # context['icon_weekly_first_day'] = str(data_weekly['list'][0]['weather'][0]['icon'])
        # context['date_weekly_first_day'] = str(data_weekly['list'][0]['dt_txt'])
        #
        # context['temperature_weekly_second_day'] = str(data_weekly['list'][1]['main']['temp']) + ' ℃'
        # context['pressure_weekly_second_day'] = str(data_weekly['list'][1]['main']['pressure'])
        # context['humidity_weekly_second_day'] = str(data_weekly['list'][1]['main']['humidity'])
        # context['temp_min_weekly_second_day'] = str(data_weekly['list'][1]['main']['temp_min']) + ' ℃'
        # context['temp_max_weekly_second_day'] = str(data_weekly['list'][1]['main']['temp_max']) + ' ℃'
        # context['feels_like_weekly_second_day'] = str(data_weekly['list'][1]['main']['feels_like']) + ' ℃'
        # context['speed_weekly_second_day'] = str(data_weekly['list'][1]['wind']['speed']) + ' mph'
        # context['description_weekly_second_day'] = str(data_weekly['list'][1]['weather'][0]['description'])
        # context['icon_weekly_second_day'] = str(data_weekly['list'][1]['weather'][0]['icon'])
        # context['date_weekly_second_day'] = str(data_weekly['list'][1]['dt_txt'])
        #
        # context['temperature_weekly_third_day'] = str(data_weekly['list'][2]['main']['temp']) + ' ℃'
        # context['pressure_weekly_third_day'] = str(data_weekly['list'][2]['main']['pressure'])
        # context['humidity_weekly_third_day'] = str(data_weekly['list'][2]['main']['humidity'])
        # context['temp_min_weekly_third_day'] = str(data_weekly['list'][2]['main']['temp_min']) + ' ℃'
        # context['temp_max_weekly_third_day'] = str(data_weekly['list'][2]['main']['temp_max']) + ' ℃'
        # context['feels_like_weekly_third_day'] = str(data_weekly['list'][2]['main']['feels_like']) + ' ℃'
        # context['speed_weekly_third_day'] = str(data_weekly['list'][2]['wind']['speed']) + ' mph'
        # context['description_weekly_third_day'] = str(data_weekly['list'][2]['weather'][0]['description'])
        # context['icon_weekly_third_day'] = str(data_weekly['list'][2]['weather'][0]['icon'])
        # context['date_weekly_third_day'] = str(data_weekly['list'][2]['dt_txt'])
        #
        # context['temperature_weekly_fourth_day'] = str(data_weekly['list'][3]['main']['temp']) + ' ℃'
        # context['pressure_weekly_fourth_day'] = str(data_weekly['list'][3]['main']['pressure'])
        # context['humidity_weekly_fourth_day'] = str(data_weekly['list'][3]['main']['humidity'])
        # context['temp_min_weekly_fourth_day'] = str(data_weekly['list'][3]['main']['temp_min']) + ' ℃'
        # context['temp_max_weekly_fourth_day'] = str(data_weekly['list'][3]['main']['temp_max']) + ' ℃'
        # context['feels_like_weekly_fourth_day'] = str(data_weekly['list'][3]['main']['feels_like']) + ' ℃'
        # context['speed_weekly_fourth_day'] = str(data_weekly['list'][3]['wind']['speed']) + ' mph'
        # context['description_weekly_fourth_day'] = str(data_weekly['list'][3]['weather'][0]['description'])
        # context['icon_weekly_fourth_day'] = str(data_weekly['list'][3]['weather'][0]['icon'])
        # context['date_weekly_fourth_day'] = str(data_weekly['list'][3]['dt_txt'])
        #
        # context['temperature_weekly_fifth_day'] = str(data_weekly['list'][4]['main']['temp']) + ' ℃'
        # context['pressure_weekly_fifth_day'] = str(data_weekly['list'][4]['main']['pressure'])
        # context['humidity_weekly_fifth_day'] = str(data_weekly['list'][4]['main']['humidity'])
        # context['temp_min_weekly_fifth_day'] = str(data_weekly['list'][4]['main']['temp_min']) + ' ℃'
        # context['temp_max_weekly_fifth_day'] = str(data_weekly['list'][4]['main']['temp_max']) + ' ℃'
        # context['feels_like_weekly_fifth_day'] = str(data_weekly['list'][4]['main']['feels_like']) + ' ℃'
        # context['speed_weekly_fifth_day'] = str(data_weekly['list'][4]['wind']['speed']) + ' mph'
        # context['description_weekly_fifth_day'] = str(data_weekly['list'][4]['weather'][0]['description'])
        # context['icon_weekly_fifth_day'] = str(data_weekly['list'][4]['weather'][0]['icon'])
        # context['date_weekly_fifth_day'] = str(data_weekly['list'][4]['dt_txt'])

        return context
