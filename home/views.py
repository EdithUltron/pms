from django.shortcuts import redirect, render
from login.models import loginForm,Login
import logging

def home(request):
    name=request.session.get("name")
    islogin=request.session.get("islogin")
    if not islogin:
        return redirect("/login/")
    logging.error(not islogin)
    return render(request,'home/home.html',{"form":{"name":name,"islogin":islogin}})

def profileaction(request):
    context={}
    sys=request.POST.get('sys',None)
    context['sys']=sys
    return render(request,'home/profile.html',context)

def placementaction(request):
    context={}
    sys=request.POST.get('sys',None)
    context['sys']=sys
    return render(request,'home/placement.html',context)

def highereducationaction(request):
    context={}
    sys=request.POST.get('sys',None)
    context['sys']=sys
    return render(request,'home/highereducation.html',context)

def detailsaction(request):
    context={}
    id=request.session.get("id")
    context=Login.objects.get(id=id).get_data()["data"]
    logging.error(context)
    return render(request,'home/details.html',{"form":context})