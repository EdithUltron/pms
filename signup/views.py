from django.shortcuts import render

def signaction(request):
    return render(request,'signup_page.html')