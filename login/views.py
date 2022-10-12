from django.shortcuts import redirect, render
from .models import loginForm,Login
import logging
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages

def loginaction(request):
    logging.error("Inside Login")
    logging.error(request)
        # logging.error(request.POST)
        # logging.error(login.is_valid())
        # logging.error(Login.objects.all())
        # logging.error(check_password(request.POST["password"],password))

    if request.method =="POST" :
        email=request.POST['email']
        # password=make_password(request.POST['password'])
        for det in Login.objects.all():

            logging.error(det.email)
            if email==det.email:
                password=det.password
                if check_password(request.POST["password"],password):   
                    login=Login(request.POST)  
                    messages.success(request,f"Login Successful")
                    logging.error("Login Successful")
                    return redirect("/",{'form':login})
                else:
                    messages.error(request,"Incorrect Password")
            else:
                messages.error(request,f"Email {email} does not exist, Do signup first")
    else:
        login=loginForm()
        # login.save()
    #    print(request.POST) 

    return render(request,'login/login_page.html',{'form':login})