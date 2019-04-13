from django.shortcuts import render
from royalFlight.db import mydb

path = "userFlights/templates/"

def index(request):
    return render(request, template_name=path + "index.html")


def gotoreserve(request):
    return render(request, template_name=path + "reserve.html")


def reservequery(request):
    return render(request, template_name=path + "index.html")

