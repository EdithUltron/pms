from django.shortcuts import render
import logging

def loginaction(request):
    logging.error("Inside Login")
    if request.method =="POST" :
        logging.error(request.POST)
    #    print(request.POST) 

    return render(request,'login/login_page.html')