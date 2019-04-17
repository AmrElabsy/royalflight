from django.shortcuts import render
from royalFlight.db import mydb

path = "planes/templates/"

def index(request):
    stmt = mydb.cursor()

    stmt.execute("SELECT * FROM planes")
    result = stmt.fetchall()
    context = {
        "planes": result
    }
    return render(request, template_name=path + "index.html", context=context)


def gotoedit(request, plane_id):
    stmt = mydb.cursor()
    stmt.execute("SELECT * FROM planes WHERE pln_ID = " + str(plane_id))
    result = stmt.fetchone()
    context = {
        "plane": result,
    }

    return render(request, template_name=path + "edit.html", context=context)


def editquery(request):
    stmt = mydb.cursor()

    if request.POST:
        id = request.POST['id_plane']
        plane_name = request.POST['pln_name']
        ca = request.POST['capacityA']
        cb = request.POST['capacityB']
        cc = request.POST['capacityC']

        sql = "UPDATE planes SET pln_name = %s, pln_c_a = %s, pln_c_b = %s, pln_c_c = %s WHERE pln_ID = %s"
        val = (plane_name, ca, cb, cc, id)
        stmt.execute(sql, val)
        mydb.commit()

    stmt.execute("SELECT * FROM planes")
    result = stmt.fetchall()
    context = {
        "planes": result,
    }
    return render(request, template_name=path + "index.html", context=context)


def gotoadd(request):
    return render(request, template_name=path + "add.html")


def addquery(request):
    stmt = mydb.cursor()

    if request.POST:
        plane_name = request.POST['pln_name']
        ca = request.POST['capacityA']
        cb = request.POST['capacityB']
        cc = request.POST['capacityC']

        sql = "INSERT INTO planes(pln_name, pln_c_a, pln_c_b, pln_c_c) VALUES (%s, %s, %s, %s)"
        val = (plane_name, ca, cb, cc)

        stmt.execute(sql, val)
        mydb.commit()

    stmt.execute("SELECT * FROM planes")
    result = stmt.fetchall()
    context = {
        "planes": result
    }
    return render(request, template_name=path + "index.html", context=context)

