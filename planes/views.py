from django.shortcuts import render
from royalFlight.db import mydb

path = "planes/templates/"

def index(request):
    return render(request, template_name=path + "index.html")


def gotoedit(request):
    return render(request, template_name=path + "edit.html")


def editquery(request):
    return render(request, template_name=path + "index.html")


def gotoadd(request):
    return render(request, template_name=path + "add.html")


def addquery(request):
    return render(request, template_name=path + "index.html")
