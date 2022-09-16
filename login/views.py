from django.shortcuts import render

def loginaction(request):
    return render(request,'login_page.html')

#Since both performs same action can be removed,and login action can be used.
# def login_styles(request):
#     return render(request,'login_page.html')