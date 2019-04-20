from django.shortcuts import render
from royalFlight.db import mydb

path = "timeTable/templates/"

def index(request):
    return render(request, template_name=path + "index.html")


def gotoedit(request):
    return render(request, template_name=path + "edit.html")


def editquery(request):
    return render(request, template_name=path + "index.html")


def gotoadd(request):
    stmt = mydb.cursor()
    stmt.execute("SELECT * FROM planes")
    result = stmt.fetchall()
    context = {
        "planes": result,
    }
    return render(request, template_name=path + "add.html", context=context)


def addquery(request):
    return render(request, template_name=path + "index.html")
