from django.shortcuts import render

def signaction(request):
    return render(request,'signup/signup_page.html')