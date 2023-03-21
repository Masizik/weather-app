from django import forms

from WeatherApp.weather_app.models import HistoryModel


class CreateHistoryModel(forms.ModelForm):
    class Meta:
        model = HistoryModel
        fields = '__all__'
