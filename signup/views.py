from django.shortcuts import render
import logging
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from .models import Register,RegisterForm

def signaction(request):


    if request.method =="POST" :
        email=request.POST['email']
        password=make_password(request.POST['password'])
        for det in Register.objects.all():

            logging.error(det.email)
            if email==det.email:
                messages.error(request,f"Email {email} already exists")
            else:
                login=RegisterForm(request.POST)
                if login.is_valid():
                    # log=Login()
                    # log.insert(email,password)
                    # log.save()
                    messages.success(request,f"Email registered")
                    logging.error("Login Successful")
    else:
        login=RegisterForm()

    return render(request,'signup/signup_page1.html')

