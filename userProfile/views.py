from django.shortcuts import render
from royalFlight.db import mydb

path = "userProfile/templates/"


def index(request):
    return render(request, template_name=path + "index.html")


def gotoedit(request):
    return render(request, template_name=path + "edit.html")


def editquery(request):
    return render(request, template_name=path + "index.html")


def tranactions(request):
    return render(request, template_name=path + "myTransactions.html")


def gotoeditreservation(request):  # go to edit reservation
    return render(request, template_name=path + "editReservation.html")


def editreservationquery(request):  # edit reservation query
    return render(request, template_name=path + "index.html")
