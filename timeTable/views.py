from django.shortcuts import render
from royalFlight.db import mydb

path = "timeTable/templates/"

def index(request):
    stmt = mydb.cursor()
    stmt.execute("SELECT timetable.*, planes.pln_name FROM timetable INNER JOIN planes ON timetable.tt_plane_id = planes.pln_ID ORDER BY tt_ID ASC")
    result = stmt.fetchall()
    context = {
        "times": result,
    }

    return render(request, template_name=path + "index.html", context=context)


def gotoedit(request, time_table_id):
    stmt = mydb.cursor()
    stmt.execute("SELECT * FROM timetable WHERE tt_ID = " + str(time_table_id))
    result = stmt.fetchone()
    context = {
        "time": result,
    }

    stmt.execute("SELECT * FROM planes")
    result = stmt.fetchall()
    context['planes'] = result

    return render(request, template_name=path + "edit.html", context=context)


def editquery(request):
    stmt = mydb.cursor()

    if request.POST:
        id_time = request.POST['time_id']
        day = request.POST['day']
        starttime = request.POST['starttime']
        endtime = request.POST['endtime']
        plane = request.POST['plane']
        origin = request.POST['origin']
        destination = request.POST['destination']
        pa = request.POST['priceA']
        pb = request.POST['priceB']
        pc = request.POST['priceC']

        sql = "UPDATE timetable SET tt_plane_id = %s, tt_start = %s, tt_end = %s, tt_price_a = %s, tt_price_b = %s, tt_price_c = %s, tt_dayofweek = %s, tt_hour_start = %s, tt_hour_end = %s WHERE tt_ID = %s"
        val = (plane, origin, destination, pa, pb, pc, day, starttime, endtime, id_time)

        stmt.execute(sql, val)
        mydb.commit()

    stmt.execute(
        "SELECT timetable.*, planes.pln_name FROM timetable INNER JOIN planes ON timetable.tt_plane_id = planes.pln_ID ORDER BY tt_ID ASC")
    result = stmt.fetchall()
    context = {
        "times": result,
    }

    return render(request, template_name=path + "index.html", context=context)


def gotoadd(request):
    stmt = mydb.cursor()
    stmt.execute("SELECT * FROM planes")
    result = stmt.fetchall()
    context = {
        "planes": result,
    }
    return render(request, template_name=path + "add.html", context=context)


def addquery(request):
    stmt = mydb.cursor()
    if request.POST:
        day = request.POST['day']
        starttime = request.POST['starttime']
        endtime = request.POST['endtime']
        plane = request.POST['plane']
        origin = request.POST['origin']
        destination = request.POST['destination']
        pa = request.POST['priceA']
        pb = request.POST['priceB']
        pc = request.POST['priceC']

        sql = 'INSERT INTO timetable(tt_plane_id, tt_start, tt_end, tt_price_a, tt_price_b, tt_price_c, tt_dayofweek, tt_hour_start, tt_hour_end) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (plane, origin, destination, pa, pb, pc, day, starttime, endtime)
        stmt.execute(sql, val)
        mydb.commit()

    stmt.execute("SELECT timetable.*, planes.pln_name FROM timetable INNER JOIN planes ON timetable.tt_plane_id = planes.pln_ID ORDER BY tt_ID ASC")
    result = stmt.fetchall()
    context = {
        "times": result,
    }

    return render(request, template_name=path + "index.html", context=context)
