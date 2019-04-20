from django.shortcuts import render
from royalFlight.db import mydb
import hashlib

path = "signInUp/templates/"


def index(request):
    return render(request, template_name=path + "index.html")


def signin(request):
    stmt = mydb.cursor()
    """
    if request.POST:
        name = request.POST['name']
        pssword = request.POST['password']
    
        stmt.execute("SELECT * FROM client WHERE clnt_name = %s AND clnt_pass = %s", (name, pssword))
        result = stmt.fetchone()
        if result:
            request.session['client'] = name
            request.session['clientid'] = result[0]
        else:
            request.session['msg'] = "<div class='alert alert-danger'>Something is Wrong</div>"
        
        context = {}
        
        if request.session['msg']:
            context['msg'] = request.session['msg']
            del request.session['msg']
    """

    return render(request, template_name="main/templates/index.html")


def signup(request):
    """
    if request.POST:
        name = request.POST['name']
        mail = request.POST['mail']
        pass1 = request.POST['pass']
        pass2 = request.POST['re-pass']
        phone = request.POST['phone']
        address = request.POST['address']
        ccNo = request.POST['credit']

        if pass1 == pass2:
            sql = "INSERT INTO client() VALUES "
            val = (name, mail, pass1, phone, address, ccNo)

            stmt.execute(sql, val)
            mydb.commit()
        else:
            request.session['msg'] = "<div class='alert alert-danger'>Two Password don't match</div>"
    """
    context = {}
    if request.session['msg']:
        context['msg'] = request.session['msg']
        del request.session['msg']

    return render(request, template_name="main/templates/index.html", context=context)

def logout(request):
    if request.session['client']:
        del request.session['client']
        del request.session['clientid']

    if request.session['Admin']:
        del request.session['Admin']
        del request.session['Adminid']

    return render(request, template_name="main/templates/index.html")
