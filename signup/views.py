import os
from dotenv import load_dotenv
from urllib import response
from django.shortcuts import redirect, render
import logging
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from .models import Register,RegisterForm,AdminRegister,AdminRegisterForm,FacultyRegisterForm,FacultyRegister
from login.models import Login,FacultyLogin,Facultyloginform
from home.models import Additional


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
            roll=request.POST['roll']
            register=RegisterForm(request.POST or None)
            # logging.error(register.password)
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
                    addi=Additional(register=inst)
                    addi.save()
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

def changepassword(request):
    id=request.session.get("id")
    user=Login.objects.get(id=id)
    context=user.get_data()["data"]
    reg=Register.objects.get(id=context["reg_id"])

    if request.method=="POST":
        pwd=request.POST.get("cpassword",None)
        pwd1=request.POST.get("c1password",None)
        pwd2=request.POST.get("c2password",None)
        opwd=reg.password
        logging.error(opwd)
        logging.error(make_password(pwd))
        if check_password(pwd,opwd):
            logging.error("success")
            if pwd1!="" or pwd2!="":
                if pwd1==pwd2:
                    pwd1=make_password(pwd1)
                    reg.update_pass(pwd1)
                    user.password=pwd1
                    user.save()
                    reg.save()
                    messages.success(request,f'Password Changed Successfully')
                else:
                    messages.error(request,f'Password Mismatch')
            else:
                messages.error(request,f'Password cant be empty')
        else:
            messages.error(request,f'Incorrect password')
        
    return render(request,'signup/changepassword.html')


def adminsignup(request):

    adm=AdminRegisterForm()
    islog=request.session.get("adminlogin",False)
    if islog:
        logging.error("Logged in already")
        return redirect("/adminpage/")

    # logging.error(request.session.__dict__)

    if request.method =="POST":
        key=request.POST.get("key")
        if request.session.get("cango",False):
            del request.session["cango"]
        logging.error(request.session)
        logging.error("Hello")
        load_dotenv()

        # You can now use the environment variables in your code
        akey = os.getenv('KEY')
        # logging.error(akey)
        # logging.error(key)
        if key==akey:
            request.session["cango"]=True
            return redirect("/adminlogin/")
        else:
            messages.error(request,f'Key Conflict')
            return redirect("/adminsignup/")

    cango=request.session.get("cango",False)
    if cango:
        return render(request,'signup/adminsignup.html',{'form':adm})

    return render(request,'signup/keypage.html')


def facultysignup(request):

    islog=request.session.get("isflogin",False)
    if islog:
        logging.error("Logged in already")
        return redirect("/facultyhome")

    if request.method =="POST" :
        if request.POST['password'] == request.POST['cpassword']:
            email=request.POST['email']
            password=make_password(request.POST['password'])
            # request.POST['password']=password
            # register.update_pass(password)
            # roll=request.POST['roll']
            register=FacultyRegisterForm(request.POST or None)
            # logging.error(register.password)
            # logging.error(register.data)
            # logging.error(request)
            logging.error(len(FacultyRegister.objects.filter(email=email).values()))
            if len(FacultyRegister.objects.filter(email=email).values())!=0:
                messages.error(request,f"Email {email} already exists")
                
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
                    # addi=Additional(register=inst)
                    # addi.save()
                    log=FacultyLogin(register=inst,email=email,password=password)
                    log.save()
                    messages.success(request,f"Email registered")
                    logging.error("SignUp Successful")
                    return render(request,'login/facultypage.html',{'form':log})
                else:
                    logging.error("not valid")
                    logging.error(register.is_valid())
        else:
            messages.error(request,"Passwords are not matched")
            register=FacultyRegisterForm()
    else:
        register=FacultyRegisterForm()

    return render(request,'signup/facultysignup.html')