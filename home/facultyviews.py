from django.shortcuts import redirect, render
from login.models import FacultyLogin
from signup.models import FacultyRegister
from .facultymodels import FacultyEducation
from .facultyforms import EducationForm
import logging
from django.contrib import messages
from functools import wraps
from login.views import facultylogout
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404
import json
from django.contrib.contenttypes.models import ContentType

def f_login(func):
    @wraps(func)
    def wrapper_func(request,*args, **kwargs):
        # logging.error(kwargs)
        # logging.error(args)
        # logging.error(kwargs.get("name",None))
        # logging.error("hello")
        if request.session.get("isflogin"):
            return func(request, *args,**kwargs)
        else:
            return redirect("/facultylogin")
    return wrapper_func

@f_login
def facultyhome(request):
    # facultylogout(request)
    return render(request,"home/faculty/facultyhome.html")

@f_login
def facultymainprofile(request):
    return render(request,"home/faculty/facultymainprofile.html")

@f_login
def facultydetails(request):
    id=request.session.get("id")
    user=FacultyLogin.objects.get(id=id)
    context=user.getDetails()["data"]
    logging.error(context)
    return render(request,"home/faculty/fprofile/facultybasicdetails.html",{"form":context})

@f_login
def facultydetailsedit(request):
    context={}
    id=request.session.get("id")
    user=FacultyLogin.objects.get(id=id)
    context=user.get_data()["data"]
    reg=FacultyRegister.objects.get(id=context["reg_id"])
    # logging.error(user.get_data())
    logging.error(context)
    logging.error(request.FILES)
    logging.error(dir(request.FILES))

    if request.method=="POST":
        p=request.FILES.get("profile_pic",context['profile_pic'])
        logging.error(p)
        reg.update(request.POST.get("aboutme",context['aboutme']),request.POST.get("fullname",context['fullname']),request.POST.get("email",context['email']),request.POST.get("department",context['department']),request.POST.get("phone",context['phone']),pp=p)
        logging.error(request.POST.get("fullname",context['fullname']))
        reg.save()
        messages.success(request,f"Details Saved")
        return redirect("/fprofileedit/facultydetails/")

    return render(request,'home/faculty/fprofileedit/facultybasicdetails.html',{"form":context})

@f_login
def facultyeducation(request):
    id=request.session.get("id")
    user=FacultyLogin.objects.get(id=id)
    context=user.get_data()["data"]
    reg=FacultyRegister.objects.get(id=context["reg_id"])
    exp=FacultyEducation.objects.filter(register=reg)
    logging.error(exp)
    form={}
    for e in exp:
        p=e.getDetails()
        logging.error(p)
        form[p["id"]]=p
    logging.error(form)
    return render(request, 'home/faculty/fprofile/education.html', {'form': form})

@f_login
def facultyeducationadd(request):
    id=request.session.get("id")
    user=FacultyLogin.objects.get(id=id)
    context=user.get_data()["data"]
    reg=FacultyRegister.objects.get(id=context["reg_id"])
    logging.error(request.POST)
    # ins=Experience.objects.get(id)
    if request.method == 'POST':
        form = EducationForm(request.POST or None )
        if form.is_valid():
            logging.error("Hello")
            inst=form.save(commit=False)
            inst.register=reg
            inst.save()
            logging.error(inst.getDetails())
            return redirect('/fprofile/facultyeducation')
        else:
            for field in form:
                logging.error(field.errors)
    else:
        form = EducationForm()
    return render(request, 'home/faculty/fprofileedit/education.html', {'form': form})

@f_login
def facultyeducationedit(request,id):
    exp=FacultyEducation.objects.get(id=int(id))

    if request.method == 'POST':
        form = EducationForm(request.POST or None ,instance=exp)
        if form.is_valid():
            form.save()
            return redirect('/fprofile/facultyeducation/')
        else:
            for field in form:
                logging.error(field.errors)
    else:
        form = EducationForm(instance=exp)
    return render(request, 'home/faculty/fprofileedit/education.html', {'form': form})

@f_login
def delete_entry(request, p , name):
    logging.error(p)
    logging.error(name)
    logging.error(name)
    # if name=="cert":
    #     content_type = Certificates
    # if name=="exp":
    #     content_type = Experience
    # if name=="hon":
    #     content_type = Awards
    # if name=="pub":
    #     content_type = Publications
    # if name=="sch":
    #     content_type = Scholarships
    if name=="edu":
        content_type = FacultyEducation
    # if name=="ski":
    #     content_type = Skills
    # if name=="lin":
    #     content_type = Links
    # if name=="pro":
    #     content_type = Projects
    # if name=="act":
    #     content_type = Activities
    
    Entry=content_type.objects.get(id=p)
    if name=='cert':
        fname=Entry.certificate_file
        inst=Entry.content_object
        if fname:
            logging.error(Entry.getDetails())
            logging.error(fname)
            Entry.certificate_file.storage.delete(fname.name)
        cnt=inst.cert_count
        inst.cert_count=cnt-1
        inst.save()
    # if name=="exp" or name=="hon" or name=="pub" or name=="sch" or name== "edu":
    #     cnt=Entry.cert_count
    #     Entry.cert_count=cnt-1
    #     Entry.save()
    logging.error(Entry)
    entry = get_object_or_404(content_type, pk=p)
    entry.delete()
    return JsonResponse({'success': True})