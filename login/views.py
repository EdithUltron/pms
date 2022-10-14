from django.shortcuts import HttpResponse, redirect, render
from .models import loginForm,Login
import logging
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages

def loginaction(request):
    # logging.error("Inside Login")
    # logging.error(request)
        # logging.error(request.POST)
        # logging.error(login.is_valid())
        # logging.error(Login.objects.all())
        # logging.error(check_password(request.POST["password"],password))
    islog=request.session.get("islogin",False)
    if islog:
        logging.error("Logged in already")
        return redirect("/")

    if request.method =="POST" :
        email=request.POST['email']
        login=Login(request.POST)  
        # password=make_password(request.POST['password'])
        for det in Login.objects.all():

            logging.error(det.register)
            if email==det.email:
                password=det.password
                if check_password(request.POST["password"],password):   
                    messages.success(request,f"Login Successful")
                    logging.error("Login Successful")
                    request.session["islogin"]=True
                    request.session["id"]=det.id
                    data=det.get_data()
                    request.session["name"]=data["data"]["fullname"]
                    logging.error(messages)
                    return redirect("/")
                else:
                    messages.error(request,"Incorrect Password")
        else:
            messages.error(request,f"Email {email} does not exist, Do signup first")
    else:
        login=loginForm()


    return render(request,'login/login_page.html',{'form':login})



def logoutaction(request):
    try:
      del request.session["islogin"]
      del request.session["id"]
    except:
      pass
    return redirect("/login/")
