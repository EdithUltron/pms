from django.shortcuts import render
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
        password=make_password(request.POST['password'])
        for det in Login.objects.all():

            logging.error(det.email)
            if email==det.email:
                messages.error(request,f"Email {email} already exists")
            else:
                login=loginForm(request.POST)
                if login.is_valid():
                    # log=Login()
                    # log.insert(email,password)
                    # log.save()
                    messages.success(request,f"Email registered")
                    logging.error("Login Successful")
    else:
        login=loginForm()
        # login.save()
    #    print(request.POST) 

    return render(request,'login/login_page.html',{'form':form})