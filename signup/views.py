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
            # request.POST['password']=password
            # register.update_pass(password)
            # logging.error(register.password)
            roll=request.POST['roll']
            register=RegisterForm(request.POST or None)
            # logging.error(register.data)
            # logging.error(request)
            
            if len(Register.objects.filter(email=email).values())!=0 or len(Register.objects.filter(roll=roll).values())!=0:
                logging.error(len(Register.objects.filter(email=email).values()))
                if len(Register.objects.filter(email=email).values())!=0:
                    messages.error(request,f"Email {email} already exists")
                if len(Register.objects.filter(roll=roll).values())!=0:
                    messages.error(request,f"User with {roll} already exists")
            else:
                if register.is_valid():
                    # reg=Register()
                    # reg.insert(request.POST['fullname'],request.POST['roll'],email,password,request.POST['phone'],request.POST['department'])                
                    # log.insert()
                    # log.register=inst
                    inst=register.save()
                    inst.update_pass(password)
                    inst.save()
                    logging.error(inst.get_id())
                    logging.error(password)
                    logging.error(inst.password)
                    log=Login(register=inst,email=email,password=password)
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


def setting(request):
    return render(request,'signup/settings.html')
