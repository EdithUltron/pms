from django.shortcuts import render

def loginaction(request):
    return render(request,'login/login_page.html')