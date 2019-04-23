from django.shortcuts import render
from royalFlight.db import mydb

path = "adminProfile/templates/"


def index(request):
    id = request.session['Adminid']
    stmt = mydb.cursor()
    stmt.execute("SELECT * FROM employee WHERE emp_ID = " + str(id))
    result = stmt.fetchone()
    context = {
        'admin': result,
    }
    return render(request, template_name=path + "index.html", context=context)


def gotoedit(request):
    id = request.session['Adminid']
    stmt = mydb.cursor()
    stmt.execute("SELECT * FROM employee WHERE emp_ID = " + str(id))
    result = stmt.fetchone()
    context = {
        'admin': result,
    }
    return render(request, template_name=path + "edit.html", context=context)


def editquery(request):
    stmt = mydb.cursor()

    if request.POST:
        id = request.session['Adminid']
        name = request.POST['name']
        mail = request.POST['email']
        password = request.POST['pass']
        phone = request.POST['phone']
        salary = request.POST['salary']
        role = request.POST['role']

        sql = "UPDATE employee SET emp_name = %s, emp_email = %s, emp_pass = %s, emp_phone = %s, emp_salary = %s, emp_role = %s WHERE emp_ID = %s"
        val = (name, mail, password, phone, salary, role, id)

        stmt.execute(sql, val)
        mydb.commit()

    id = request.session['Adminid']
    stmt.execute("SELECT * FROM employee WHERE emp_ID = " + str(id))
    result = stmt.fetchone()
    context = {
        'admin': result,
    }
    return render(request, template_name=path + "index.html", context=context)

