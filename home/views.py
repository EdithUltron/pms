from django.shortcuts import redirect, render
from login.models import loginForm,Login
from signup.models import Register
from .models import Experience,Education,Skills,Projects,Awards,Publications,Scholarships,Activities,Links
from .forms import ExperienceForm,EducationForm,SkillsForm,ProjectsForm,AwardsForm,PublicationsForm,ScholarshipsForm,ActivitiesForm,LinksForm
import logging
from django.contrib import messages
from functools import wraps
from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
import json

def is_login(func):
    @wraps(func)
    def wrapper_func(request,*args, **kwargs):
        # logging.error(kwargs)
        # logging.error(args)
        # logging.error(kwargs.get("name",None))
        if request.session.get("islogin"):
            return func(request, *args,**kwargs)
        else:
            return redirect("/login")
    return wrapper_func



def home(request):
    name=request.session.get("name")
    islogin=request.session.get("islogin")
    if not islogin:
        return redirect("/login/")
    logging.error(not islogin)
    return render(request,'home/home.html',{"form":{"name":name,"islogin":islogin}})

def mainProfile(request):
    return render(request,'home/profile/mainProfile.html')

@is_login
def details(request):
    id=request.session.get("id")
    user=Login.objects.get(id=id)
    context=user.getDetails()["data"]
    logging.error(context)
    return render(request,'home/profile/details.html',{"form":context})

@is_login
def detailsedit(request):
    context={}
    id=request.session.get("id")
    user=Login.objects.get(id=id)
    context=user.get_data()["data"]
    reg=Register.objects.get(id=context["reg_id"])
    # logging.error(user.get_data())
    # logging.error(context)
    # logging.error(request.FILES)
    # logging.error(dir(request.FILES))

    if request.method=="POST":
        p=request.FILES.get("profile_pic",None)
        logging.error(p)
        reg.update(request.POST.get("aboutme",context['aboutme']),request.POST.get("fullname",context['fullname']),request.POST.get("roll",context['roll']),request.POST.get("email",context['email']),request.POST.get("department",context['department']),request.POST.get("phone",context['phone']),pp=p)
        logging.error(request.POST.get("fullname",context['fullname']))
        reg.save()
        messages.success(request,f"Details Saved")
        return redirect("/profileedit/details/")

    return render(request,'home/profileedit/details.html',{"form":context})

@is_login
def education(request):
    pass

@is_login
def educationedit(request):
    id=request.session.get("id")
    user=Login.objects.get(id=id)
    context=user.get_data()["data"]
    reg=Register.objects.get(id=context["reg_id"])
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
            return redirect('/mainprofile/')
        else:
            for field in form:
                logging.error(field.errors)
    else:
        form = EducationForm()
    return render(request, 'home/profileedit/education.html', {'form': form})


@is_login
def experience(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        p = data['id']
        logging.error(p)
        return delete_entry(request,p)

    id=request.session.get("id")
    user=Login.objects.get(id=id)
    context=user.get_data()["data"]
    reg=Register.objects.get(id=context["reg_id"])
    exp=Experience.objects.filter(register=reg)
    logging.error(exp)
    form={}
    for e in exp:
        p=e.getDetails()
        logging.error(p)
        form[p["id"]]=p
    logging.error(form)
    return render(request, 'home/profile/experience.html', {'form': form})


@is_login
def experienceedit(request):
    id=request.session.get("id")
    user=Login.objects.get(id=id)
    context=user.get_data()["data"]
    reg=Register.objects.get(id=context["reg_id"])
    logging.error(request.POST)
    # ins=Experience.objects.get(id)
    if request.method == 'POST':
        form = ExperienceForm(request.POST or None )
        if form.is_valid():
            logging.error("Hello")
            inst=form.save(commit=False)
            inst.register=reg
            inst.save()
            logging.error(inst.getDetails())
            return redirect('/mainprofile/')
        else:
            for field in form:
                logging.error(field.errors)
    else:
        form = ExperienceForm()
    return render(request, 'home/profileedit/experience.html', {'form': form})

def delete_entry(request, p):
    Entry=Experience.objects.get(id=p)
    logging.error(Entry)
    entry = get_object_or_404(Experience, pk=p)
    entry.delete()
    return JsonResponse({'success': True})

@is_login
def skills(request):
    pass

@is_login
def skillsedit(request):
    id=request.session.get("id")
    user=Login.objects.get(id=id)
    context=user.get_data()["data"]
    reg=Register.objects.get(id=context["reg_id"])
    logging.error(request.POST)
    # ins=Experience.objects.get(id)
    if request.method == 'POST':
        form = SkillsForm(request.POST or None )
        if form.is_valid():
            logging.error("Hello")
            inst=form.save(commit=False)
            inst.register=reg
            inst.save()
            logging.error(inst.getDetails())
            return redirect('/mainprofile/')
        else:
            for field in form:
                logging.error(field.errors)
    else:
        form = SkillsForm()
    return render(request, 'home/profileedit/skills.html', {'form': form})

@is_login
def projects(request):
    pass

@is_login
def projectsedit(request):
    id=request.session.get("id")
    user=Login.objects.get(id=id)
    context=user.get_data()["data"]
    reg=Register.objects.get(id=context["reg_id"])
    logging.error(request.POST)
    # ins=Experience.objects.get(id)
    if request.method == 'POST':
        form = ProjectsForm(request.POST or None )
        if form.is_valid():
            logging.error("Hello")
            inst=form.save(commit=False)
            inst.register=reg
            inst.save()
            logging.error(inst.getDetails())
            return redirect('/mainprofile/')
        else:
            for field in form:
                logging.error(field.errors)
    else:
        form = ProjectsForm()
    return render(request, 'home/profileedit/projects.html', {'form': form})


@is_login
def awards(request):
    pass

@is_login
def awardsedit(request):
    id=request.session.get("id")
    user=Login.objects.get(id=id)
    context=user.get_data()["data"]
    reg=Register.objects.get(id=context["reg_id"])
    logging.error(request.POST)
    # ins=Experience.objects.get(id)
    if request.method == 'POST':
        form = AwardsForm(request.POST or None )
        if form.is_valid():
            logging.error("Hello")
            inst=form.save(commit=False)
            inst.register=reg
            inst.save()
            logging.error(inst.getDetails())
            return redirect('/mainprofile/')
        else:
            for field in form:
                logging.error(field.errors)
    else:
        form = AwardsForm()
    return render(request, 'home/profileedit/awards.html', {'form': form})


@is_login
def publications(request):
    pass

@is_login
def publicationsedit(request):
    id=request.session.get("id")
    user=Login.objects.get(id=id)
    context=user.get_data()["data"]
    reg=Register.objects.get(id=context["reg_id"])
    logging.error(request.POST)
    # ins=Experience.objects.get(id)
    if request.method == 'POST':
        form = PublicationsForm(request.POST or None )
        if form.is_valid():
            logging.error("Hello")
            inst=form.save(commit=False)
            inst.register=reg
            inst.save()
            logging.error(inst.getDetails())
            return redirect('/mainprofile/')
        else:
            for field in form:
                logging.error(field.errors)
    else:
        form = PublicationsForm()
    return render(request, 'home/profileedit/publications.html', {'form': form})


@is_login
def scholarships(request):
    pass

@is_login
def scholarshipsedit(request):
    id=request.session.get("id")
    user=Login.objects.get(id=id)
    context=user.get_data()["data"]
    reg=Register.objects.get(id=context["reg_id"])
    logging.error(request.POST)
    # ins=Experience.objects.get(id)
    if request.method == 'POST':
        form = ScholarshipsForm(request.POST or None )
        if form.is_valid():
            logging.error("Hello")
            inst=form.save(commit=False)
            inst.register=reg
            inst.save()
            logging.error(inst.getDetails())
            return redirect('/mainprofile/')
        else:
            for field in form:
                logging.error(field.errors)
    else:
        form = ScholarshipsForm()
    return render(request, 'home/profileedit/scholarships.html', {'form': form})


@is_login
def activities(request):
    pass

@is_login
def activitiesedit(request):
    id=request.session.get("id")
    user=Login.objects.get(id=id)
    context=user.get_data()["data"]
    reg=Register.objects.get(id=context["reg_id"])
    logging.error(request.POST)
    # ins=Experience.objects.get(id)
    if request.method == 'POST':
        form = ActivitiesForm(request.POST or None )
        if form.is_valid():
            logging.error("Hello")
            inst=form.save(commit=False)
            inst.register=reg
            inst.save()
            logging.error(inst.getDetails())
            return redirect('/mainprofile/')
        else:
            for field in form:
                logging.error(field.errors)
    else:
        form = ActivitiesForm()
    return render(request, 'home/profileedit/activities.html', {'form': form})


@is_login
def links(request):
    pass

@is_login
def linksedit(request):
    id=request.session.get("id")
    user=Login.objects.get(id=id)
    context=user.get_data()["data"]
    reg=Register.objects.get(id=context["reg_id"])
    logging.error(request.POST)
    # ins=Experience.objects.get(id)
    if request.method == 'POST':
        form = LinksForm(request.POST or None )
        if form.is_valid():
            logging.error("Hello")
            inst=form.save(commit=False)
            inst.register=reg
            inst.save()
            logging.error(inst.getDetails())
            return redirect('/mainprofile/')
        else:
            for field in form:
                logging.error(field.errors)
    else:
        form = LinksForm()
    return render(request, 'home/profileedit/links.html', {'form': form})


# def profileaction(request):
#     context=Register.objects.all()
#     return render(request,'home/profile.html',{"persons":context})


# def placementaction(request):
#     # logging.error(dir(request.user))
#     # logging.error(request.user.password)
#     context={}
#     id=request.session.get("id")
#     user=Login.objects.get(id=id)
#     context=user.get_data()["data"]
#     reg=Register.objects.get(id=context["reg_id"])
#     logging.error(user.get_data())
#     logging.error(context)

#     if request.method=="POST":
#         reg.update(request.POST.get("fullname",context['fullname']),request.POST.get("roll",context['roll']),request.POST.get("email",context['email']),request.POST.get("department",context['department']),request.POST.get("phone",context['phone']))
#         reg.save()
#         messages.success(request,f"Details Saved")
#         return redirect("/details")
#     return render(request,'home/placement.html',{"form":context})

# def highereducationaction(request):
#     context={}
#     id=request.session.get("id")
#     user=Login.objects.get(id=id)
#     context=user.get_data()["data"]
#     reg=Register.objects.get(id=context["reg_id"])
#     logging.error(user.get_data())
#     logging.error(context)

#     if request.method=="POST":
#         reg.update(request.POST.get("fullname",context['fullname']),request.POST.get("roll",context['roll']),request.POST.get("email",context['email']),request.POST.get("department",context['department']),request.POST.get("phone",context['phone']))
#         reg.save()
#         messages.success(request,f"Details Saved")
#         return redirect("/details")
#     return render(request,'home/highereducation.html',{"form":context})
