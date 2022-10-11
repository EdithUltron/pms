from statistics import mode
from django.db import models
from django import forms


# Create your models here.

class Register(models.Model):
    fullName = models.CharField("Full name", max_length=255, blank = True, null = True)
    roll=models.CharField(max_length=10, blank = True, null = True)
    email=models.EmailField(max_length=150,unique=True,null=False)
    password=models.CharField(max_length=200,null=False)
    phone = models.CharField(max_length=20, blank = True, null = True)
    department = models.CharField(null=False)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.fullName

class RegisterForm(forms.Form):
    class Meta:
        model=Register
        fields = "__all__"
        widgets = {
            'password':forms.PasswordInput()
        }
    
    def __str__(self) -> str:
        return "Register form"