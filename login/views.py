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
            request.session["adminbranch"]=id.department
            request.session["adminid"]=id.id
            return redirect("/adminpage/")

    cango=request.session.get("cango",False)
    if cango:
        return render(request,'login/adminlogin.html',{'form':form})
    
    return render(request,'signup/keypage.html')

    
def adminpage(request):
    islog=request.session.get("adminlogin",False)
    if not islog:
        return redirect("/adminlogin/")

    adid=request.session.get("adminid")
    adbranch=request.session.get("adminbranch")
    logging.error(adbranch)
    stu=Register.objects.filter(department=adbranch)
    logging.error(stu)
    # logging.error(stu.values())
    logging.error(request.POST)
    logging.error(len(request.POST))
    form={}
    for i in stu.values():
        form[i["id"]]=i
        # p=i.get_data()

    if request.method=="POST" and len(request.POST)>2:
        form={}
        logging.error(request.POST.__dict__)
        logging.error(request.POST.get("name"))

        year=request.POST.get("year")
        if(year):
            stu=Register.objects.filter(department=adbranch,year=year)   

        for i in stu:

            p=i.get_data()


            if(request.POST.get("name",None)):
                if form.get('name',None):
                    form["name"].append(p["fullname"])
                else:
                    form["name"]=[]
                    form["name"].append(p["fullname"])

            if(request.POST.get("roll",None)):
                if form.get('roll',None):
                    form["roll"].append(p["roll"])
                else:
                    form["roll"]=[]
                    form["roll"].append(p["roll"])
            
            if(request.POST.get("phone",None)):
                if form.get('phone',None):
                    form["phone"].append(p["phone"])
                else:
                    form["phone"]=[]
                    form["phone"].append(p["phone"])
            
            if(request.POST.get("email",None)):
                if form.get('email',None):
                    form["email"].append(p["email"])
                else:
                    form["email"]=[]
                    form["email"].append(p["email"])
            
            if(request.POST.get("about",None)):
                if form.get('aboutme',None):
                    form["aboutme"].append(p["aboutme"])
                else:
                    form["aboutme"]=[]
                    form["aboutme"].append(p["aboutme"])
            
            if(request.POST.get("edu",None)):
                pass
            
            if(request.POST.get("internships",None)):
                pass
            
            if(request.POST.get("jobs",None)):
                pass
            
            if(request.POST.get("skills",None)):
                pass
            
            if(request.POST.get("awards",None)):
                pass
            
            if(request.POST.get("sch",None)):
                pass
            
            if(request.POST.get("links",None)):
                pass

            logging.error(form)
        

    return render(request,'login/adminpage.html',{'form':form})


def adminlogout(request):
    try:
      del request.session["cango"]
      del request.session["adminlogin"]
      del request.session["adminbranch"]
      del request.session["adminid"]
    #   del request.session["name"]
    except:
      pass
    return redirect("/adminsignup/")