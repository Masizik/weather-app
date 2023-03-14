from django.shortcuts import render
from django.views import generic as views


# Create your views here.
class IndexView(views.DetailView):
    template_name = 'index.html'
