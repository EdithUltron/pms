from urllib import response
from django.shortcuts import redirect, render
import logging
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from .models import Register,RegisterForm
from login.models import Login

def signaction(request):

    islog=request.session.get("islogin",False)
    if islog:
        logging.error("Logged in already")
        return redirect("/")

    if request.method =="POST" :
        if request.POST['password'] == request.POST['cpassword']:
            email=request.POST['email']
            password=make_password(request.POST['password'])
            roll=request.POST['roll']
            # logging.error(password)
            register=RegisterForm(request.POST)
            # register.data['password']=password
            logging.error(register.data)
            
            for det in Register.objects.all():
                logging.error(det.email)
                if email==det.email:
                    messages.error(request,f"Email {email} already exists")
                    break
                if roll==det.roll:
                    messages.error(request,f"User with {roll} already exists")
                    break
            else:
                if register.is_valid():
                    reg=Register()
                    reg.insert(request.POST['fullname'],request.POST['roll'],email,password,request.POST['phone'],request.POST['department'])                
                    inst=reg.save()
                    logging.error(reg.get_id())
                    log=Login()
                    log.insert(email,password)
                    # inst=log.save(commit=False)
                    log.register=reg
                    log.save()
                    messages.success(request,f"Email registered")
                    logging.error("SignUp Successful")
                    return render(request,'login/login_page.html',{'form':log})
                else:
                    logging.error("not valid")
                    logging.error(register.is_valid())
        else:
            messages.error(request,"Passwords are not matched")
            register=RegisterForm()
    else:
        register=RegisterForm()

    return render(request,'signup/signup_page.html',{'form':register.data})

