from django.shortcuts import render

def home(request):
    name=request.session.get("name")
    return render(request,'home/home.html',{"form":{"name":name}})

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
    sys=request.POST.get('sys',None)
    context['sys']=sys
    return render(request,'home/details.html',context)