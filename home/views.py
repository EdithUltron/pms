from django.shortcuts import render

def home(request):
    context={}
    sys=request.POST.get('sys',None)
    context['sys']=sys
    return render(request,'home/home.html',context)

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