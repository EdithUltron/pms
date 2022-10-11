from dataclasses import fields
from pyexpat import model
from django import forms
from django.db import models
# from django import forms
# Create your models here.
class Login(models.Model):
    email=models.EmailField(max_length=150)
    password=models.CharField(max_length=200)

    def insert(self,email,password):
        self.email=email
        self.password=password

    def __str__(self) -> str:
        return self.email+" : "+self.password




class loginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields = "__all__"
    
    def __str__(self) -> str:
        return "Login form"