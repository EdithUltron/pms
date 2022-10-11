from dataclasses import fields
from enum import unique
from pyexpat import model
from django import forms
from django.db import models
from signup.models import Register
# from django import forms
# Create your models here.
class Login(models.Model):
    register=models.ForeignKey(Register,on_delete=models.CASCADE)
    email=models.EmailField(max_length=150,unique=True,null=False)
    password=models.CharField(max_length=200,null=False)

    def insert(self,email,password):
        self.email=email
        self.password=password

    def __str__(self) -> str:
        return self.email+" : "+self.password




class loginForm(forms.Form):
    class Meta:
        model=Login
        fields = "__all__"
        widgets = {
            'password':forms.PasswordInput()
        }
    
    def __str__(self) -> str:
        return "Login form"