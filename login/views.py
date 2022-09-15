from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def loginaction(request):
    return render(request,'Interactive_Portal/template/login_page.html')

