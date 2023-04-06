import urllib.request

from django.shortcuts import render
from django.views import generic as views
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
        data_current = json.loads(source_current)
        source_weekly = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/forecast?q=' + city + '&units=metric&appid=720dfb1dcf0e39692ddd35603283c28a').read()
        data_weekly = json.loads(source_weekly)



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


        if city == "None":
            context['city'] = "Varna"
        else:
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

        source_pic = urllib.request.urlopen('https://pixabay.com/api/?key=35144089-69d0946cd8388cd304f30dc2e&q=' + (str(data_current['weather'][0]['description']).replace(" ", "%20")
                                                                                                                    )).read()
        source_pic_body = urllib.request.urlopen('https://pixabay.com/api/?key=35144089-69d0946cd8388cd304f30dc2e&q=' + (
            city.replace(" ", "%20")
            )).read()

        data_pic = json.loads(source_pic)
        data_pic_body = json.loads(source_pic_body)

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
        context['pic'] = data_pic['hits'][0]['webformatURL']
        context['pic_body'] = data_pic_body['hits'][0]['webformatURL']

        context['weekly_all'] = dict(enumerate(zip(context['weekly_temp'], context['weekly_description'], context['weekly_temp_max'],context['weekly_temp_min'],context['weekly_temp_feels_like'],context['weekly_humidity'],context['weekly_date'],context['weekly_pressure'],context['weekly_speed'],context['weekly_icon'])))


        return context


def error_404_view(request):
    # we add the path to the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')