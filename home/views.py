from django.shortcuts import render

def home(request):
    return render(request,'home/home.html')

def profileaction(request):
    return render(request,'home/profile.html')

def placementaction(request):
    return render(request,'home/placement.html')

def highereducationaction(request):
    return render(request,'home/highereducation.html')