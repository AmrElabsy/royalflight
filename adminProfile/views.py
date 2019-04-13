from django.shortcuts import render
from royalFlight.db import mydb

path = "adminProfile/templates/"


def index(request):
    return render(request, template_name=path + "index.html")


def gotoedit(request):   # Takes The ID of The Admin as a Parameter
    return render(request, template_name=path + "edit.html")


def editquery(request):
    return render(request, template_name=path + "index.html")

