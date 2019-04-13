from django.shortcuts import render
from royalFlight.db import mydb

path = "signInUp/templates/"


def index(request):
    return render(request, template_name=path + "index.html")


def signin(request):
    return render(request, template_name="")


def signup(request):
    return render(request, template_name="main/templates/index.html")


def logout(request):
    return render(request, template_name="main/templates/index.html")



