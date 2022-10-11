from django.shortcuts import render
from .models import loginForm
import logging

def loginaction(request):
    logging.error("Inside Login")
    # logging.error(request.POST)
    if request.method =="POST" :
        logging.error(request.POST)
        email=request.POST['email']
        password=request.POST['password']
        login=loginForm(request.POST)
        logging.error(login)
        if login.is_valid():
            login.save()
            logging.error("Login Successful")
        # login.insert(email,password)
        # login.save()
    #    print(request.POST) 

    return render(request,'login/login_page.html')