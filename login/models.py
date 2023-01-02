from django import forms
from django.db import models
from signup.models import Register,AdminRegister

# Create your models here.
class Login(models.Model):
    register=models.ForeignKey(Register,on_delete=models.CASCADE)
    email=models.EmailField(max_length=150,unique=True,null=False)
    password=models.CharField(max_length=200,null=False)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.email=self.register.email
        self.password=self.register.password

    def insert(self,email,password):
        self.email=email
        self.password=password

    def get_data(self):
        data=self.register.get_data()
        return {"email":self.email,"data":data}

    def getDetails(self):
        data=self.register.getDetails()
        return {"email":self.email,"data":data}

    def __str__(self) -> str:
        return self.email




class loginForm(forms.Form):
    class Meta:
        model=Login
        fields = "__all__"
        widgets = {
            'password':forms.PasswordInput()
        }
    
    def __str__(self) -> str:
        return "Login form"


class Adminloginform(forms.ModelForm):
    class Meta:
        model=AdminRegister
        fields=['email','password']
        widgets = {
            'password':forms.PasswordInput(),
        }

class Facultyloginform(forms.Form):
    class Meta:
        model=Login
        fields = "__all__"
        widgets = {
            'password':forms.PasswordInput()
        }
    
    def __str__(self) -> str:
        return "Faculty Login form"