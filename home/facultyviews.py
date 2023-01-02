from django.shortcuts import redirect, render
import logging
from django.contrib import messages
from functools import wraps
from login.views import facultylogout
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404
import json
from django.contrib.contenttypes.models import ContentType

def facultyhome(request):
    facultylogout(request)
    return render(request,"home/faculty/facultyhome.html")

def facultymainprofile(request):
    return render(request,"home/faculty/facultymainprofile.html")