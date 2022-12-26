from django.db import models
from django import forms

import os
import logging

def upload_to(instance, filename):
    return os.path.join("profile_pic/",instance.roll, filename)

# Create your models here.

class Register(models.Model):
    fullname = models.CharField("Full name", max_length=255, blank = True, null = True)
    roll=models.CharField(max_length=10, blank = True, null = True)
    email=models.EmailField(max_length=150,unique=True,null=False)
    password=models.CharField(max_length=200,null=False)
    phone = models.CharField(max_length=20, blank = True, null = True)
    department = models.CharField(max_length=5,null=False)
    aboutme=models.CharField(max_length=1000,default="Iam a Student",null=True,blank=True)
    profile_pic=models.ImageField(upload_to=upload_to,default="../media/profile_pic/demo_pic.png")
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def update(self,am,fn,roll,email,dept,phone,pp):
        self.aboutme=am
        self.fullname=fn
        self.roll=roll
        self.email=email
        self.phone=phone
        self.department=dept

        if self.profile_pic.name=="../media/profile_pic/demo_pic.png":
            self.profile_pic=pp
        else:
            logging.error(pp)
            if not self.profile_pic==pp and not pp==None:
                if os.path.isfile(self.profile_pic.path):
                    os.remove(self.profile_pic.path)
                self.profile_pic=pp



    def update_pass(self,pswd):
        logging.error("In update pass")
        logging.error(pswd)
        self.password=pswd
        logging.error(self.password)
            

    def get_id(self):
        return self.id

    def get_data(self):
        return {"reg_id":self.id,"aboutme":self.aboutme,"fullname":self.fullname,"email":self.email,"roll":self.roll,"phone":self.phone,"department":self.department,"profile_pic":self.profile_pic}
    
    def getDetails(self):
        return {"fullname":self.fullname,"aboutme":self.aboutme,"email":self.email,"roll":self.roll,"phone":self.phone,"department":self.department,"profile_pic":self.profile_pic}

    def __str__(self):
        return self.fullname

class RegisterForm(forms.ModelForm):
    class Meta:
        model=Register
        fields = "__all__"
        widgets = {
            'password':forms.PasswordInput(),
            'profile_pic': forms.ClearableFileInput(attrs={'multiple': True}),
        }
    
    def __str__(self) -> str:
        return "Register form"
