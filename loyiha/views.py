from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello world!</h1>")


class Dash(TemplateView):
    template_name = "dash.html"


class About(TemplateView):
    template_name = 'about.html'


class News(TemplateView):
    template_name = "news.html"
