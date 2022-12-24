from django.db import models
from signup.models import Register
from datetime import datetime
import logging
# Create your models here.
class Experience(models.Model):
    register=models.ForeignKey(Register,on_delete=models.CASCADE,default=1)
    company=models.CharField(max_length=255, blank = True, null = True)
    location=models.CharField(max_length=255, blank = True, null = True)
    role=models.CharField(max_length=255, blank = True, null = True)
    package=models.CharField(max_length=20, blank = True, null = True)
    startdate=models.DateField(default=datetime.now)
    enddate=models.DateField(default=datetime.now)
    workmode=models.CharField(max_length=10,default='1', choices=(
            ('1','Online'),
            ('2','Offline')))
    mode=models.CharField(max_length=10,default='1', choices=(
            ( '1','Oncampus'),
            ( '2','Offcampus')))
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def getDetails(self):
        data={}
        attributes = self.__dict__
        excluded_attributes = ['_state', 'createdAt']
        for attr_name, attr_value in attributes.items():
            if attr_name not in excluded_attributes:
                data[attr_name]=attr_value
        return data

    def __str__(self):
        return self.company



class Education(models.Model):
    register=models.ForeignKey(Register,on_delete=models.CASCADE,default=1)
    school=models.CharField(max_length=255, blank = True, null = True)
    location=models.CharField(max_length=255, blank = True, null = True)
    course=models.CharField(max_length=255, blank = True, null = True)
    startdate=models.DateField(default=datetime.now)
    enddate=models.DateField(default=datetime.now)
    
class Skills(models.Model):
    register=models.ForeignKey(Register,on_delete=models.CASCADE,default=1)
    skill=models.CharField(max_length=255, blank = True, null = True)
    rating=models.IntegerField()
class Projects(models.Model):
    register=models.ForeignKey(Register,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=255, blank = True, null = True)
    description=models.CharField(max_length=500, blank = True, null = True)
    url=models.CharField(max_length=255, blank = True, null = True)

class Awards(models.Model):
    register=models.ForeignKey(Register,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=255, blank = True, null = True)
    description=models.CharField(max_length=255, blank = True, null = True)
    date=models.DateField(default=datetime.now)

class Publications(models.Model):
    register=models.ForeignKey(Register,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=255, blank = True, null = True)
    description=models.CharField(max_length=255, blank = True, null = True)
    date=models.DateField(default=datetime.now)
class Scholarships(models.Model):
    register=models.ForeignKey(Register,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=255, blank = True, null = True)
    description=models.CharField(max_length=255, blank = True, null = True)
    date=models.DateField(default=datetime.now)
class Activities(models.Model):
    register=models.ForeignKey(Register,on_delete=models.CASCADE,default=1)
    # award=models.ForeignKey(Awards,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=255, blank = True, null = True)
    description=models.CharField(max_length=255, blank = True, null = True)
    date=models.DateField(default=datetime.now)
class Links(models.Model):
    register=models.ForeignKey(Register,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=255, blank = True, null = True,default='1', choices=(
            ('1','LinkedIn'),
            ('2','Github'),
            ('3','Twitter'),
            ('4','Instagram'),
            ('5','Discord'),
            ('6','Stackoverflow'),
            ('7','Portfolio'),
            ('8','Facebook')
            ))
    url=models.CharField(max_length=255, blank = True, null = True)
    
