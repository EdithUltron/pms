from django.shortcuts import HttpResponse, redirect, render
from .models import loginForm,Login,Adminloginform
import logging
from signup.models import Register
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from signup.models import AdminRegister,AdminRegisterForm

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
        login={'email':email} 
        # password=make_password(request.POST['password'])
        det=Login.objects.filter(email=email).values()
        logging.error(det)

        if len(det)!=0:

            # logging.error(det)
            # logging.error(det[0])
            # logging.error(det.register)
            if email==det[0]["email"]:
                password=det[0]['password']
                if check_password(request.POST["password"],password):   
                    messages.success(request,f"Login Successful")
                    # logging.error("Login Successful")
                    request.session["islogin"]=True
                    request.session["id"]=det[0]['id']
                    reg_id=det[0]["register_id"]
                    data=Register.objects.get(id=reg_id)
                    # logging.error(reg_id)
                    # logging.error(data.get_data())
                    data=data.get_data()
                    request.session["name"]=data["fullname"]
                    # logging.error(messages)
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
      del request.session["name"]
    except:
      pass
    return redirect("/login/")




def adminlogin(request):
    form=Adminloginform()
    islog=request.session.get("adminlogin",False)
    if islog:
        logging.error("Logged in already")
        return redirect("/adminpage/")

    if request.method =="POST":
        email=request.POST.get("email")
        pwd=request.POST.get("password")
        id=AdminRegister.objects.get(email=email)

        if id!=None and id.password==pwd:
            request.session["adminlogin"]=True
            return redirect("/adminpage/")

    cango=request.session.get("cango",False)
    if cango:
        return render(request,'login/adminlogin.html',{'form':form})
    
    return render(request,'signup/keypage.html')

    
def adminpage(request):
    islog=request.session.get("adminlogin",False)
    if not islog:
        return redirect("/adminlogin/")

    

    return render(request,'login/adminpage.html')


def adminlogout(request):
    try:
      del request.session["cango"]
      del request.session["adminlogin"]
    #   del request.session["name"]
    except:
      pass
    return redirect("/adminsignup/")