from django.db import models

# Create your models here.
class Login(models.Model):
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.email+" : "+self.password

