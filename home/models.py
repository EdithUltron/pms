from django.db import models
from signup.models import Register
from datetime import datetime
import logging
import os
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.core.validators import FileExtensionValidator
from django.contrib.contenttypes.fields import GenericRelation
from datetime import datetime
# from .models import Certificates


def upload_c_to(instance, filename):
    logging.error(instance.content_object)
    return os.path.join("certificates/",instance.content_object.register.roll, filename)
# Create your models here.

class Certificates(models.Model):
    certificate_name = models.CharField(max_length=255)
    certificate_file=models.FileField(upload_to=upload_c_to,default=None, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    

    def getDetails(self):
        data={}
        attributes = self.__dict__
        excluded_attributes = ['_state', 'createdAt']
        for attr_name, attr_value in attributes.items():
            if attr_name not in excluded_attributes:
                data[attr_name]=attr_value
        return data

    def __str__(self):
        return self.certificate_name
    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]


    

class Experience(models.Model):
    register=models.ForeignKey(Register,on_delete=models.CASCADE,default=1)
    type=models.CharField(max_length=10,default='1', choices=(
            ('1','Internship'),
            ('2','Job')))
    company=models.CharField(max_length=255, blank = True, null = True)
    location=models.CharField(max_length=255, blank = True, null = True)
    role=models.CharField(max_length=255, blank = True, null = True)
    package=models.CharField(max_length=20, blank = True, null = True)
    startdate=models.DateField(default=datetime.now)
    enddate=models.DateField(default=datetime.now)
    cert_count=models.IntegerField(default=0)
    certificates=GenericRelation(Certificates)
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
    school=models.CharField(max_length=255, blank = True, null = True,default='1', choices=(
            ( '1','High School'),
            ( '2','Intermediate'),
            ( '3','Diploma'),
            ( '4','Btech'),
            ( '5','Mtech'),
            ( '6','MCA'),
            ( '7','PG'),
            ( '8','BArch'),
            ))
    name=models.CharField(max_length=255, blank = True, null = True)
    location=models.CharField(max_length=255, blank = True, null = True)
    course=models.CharField(max_length=255, blank = True, null = True)
    startdate=models.DateField(default=datetime.now)
    enddate=models.DateField(default=datetime.now)

    def getDetails(self):
        data={}
        attributes = self.__dict__
        excluded_attributes = ['_state', 'createdAt']
        for attr_name, attr_value in attributes.items():
            if attr_name not in excluded_attributes:
                data[attr_name]=attr_value
        return data
    
class Skills(models.Model):
    register=models.ForeignKey(Register,on_delete=models.CASCADE,default=1)
    skill=models.CharField(max_length=255, blank = True, null = True)
    rating=models.CharField(max_length=10,default='1', choices=(
            ( '0','0'),
            ( '1','1'),
            ( '2','2'),
            ( '3','3'),
            ( '4','4'),
            ( '5','5'),
            ( '6','6'),
            ( '7','7'),
            ( '8','8'),
            ( '9','9'),
            ( '10','10'),
            ))

    def getDetails(self):
        data={}
        attributes = self.__dict__
        excluded_attributes = ['_state', 'createdAt']
        for attr_name, attr_value in attributes.items():
            if attr_name not in excluded_attributes:
                data[attr_name]=attr_value
        return data
    
class Projects(models.Model):
    register=models.ForeignKey(Register,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=255, blank = True, null = True)
    description=models.CharField(max_length=500, blank = True, null = True)
    url=models.CharField(max_length=255, blank = True, null = True)

    def getDetails(self):
        data={}
        attributes = self.__dict__
        excluded_attributes = ['_state', 'createdAt']
        for attr_name, attr_value in attributes.items():
            if attr_name not in excluded_attributes:
                data[attr_name]=attr_value
        return data

class Awards(models.Model):
    register=models.ForeignKey(Register,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=255, blank = True, null = True)
    description=models.CharField(max_length=255, blank = True, null = True)
    cert_count=models.IntegerField(default=0)
    date=models.DateField(default=datetime.now)

    def getDetails(self):
        data={}
        attributes = self.__dict__
        excluded_attributes = ['_state', 'createdAt']
        for attr_name, attr_value in attributes.items():
            if attr_name not in excluded_attributes:
                data[attr_name]=attr_value
        return data

class Publications(models.Model):
    register=models.ForeignKey(Register,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=255, blank = True, null = True)
    description=models.CharField(max_length=255, blank = True, null = True)
    cert_count=models.IntegerField(default=0)
    date=models.DateField(default=datetime.now)

    def getDetails(self):
        data={}
        attributes = self.__dict__
        excluded_attributes = ['_state', 'createdAt']
        for attr_name, attr_value in attributes.items():
            if attr_name not in excluded_attributes:
                data[attr_name]=attr_value
        return data
class Scholarships(models.Model):
    register=models.ForeignKey(Register,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=255, blank = True, null = True)
    description=models.CharField(max_length=255, blank = True, null = True)
    cert_count=models.IntegerField(default=0)
    date=models.DateField(default=datetime.now)

    def getDetails(self):
        data={}
        attributes = self.__dict__
        excluded_attributes = ['_state', 'createdAt']
        for attr_name, attr_value in attributes.items():
            if attr_name not in excluded_attributes:
                data[attr_name]=attr_value
        return data
class Activities(models.Model):
    register=models.ForeignKey(Register,on_delete=models.CASCADE,default=1)
    # award=models.ForeignKey(Awards,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=255, blank = True, null = True)
    description=models.CharField(max_length=255, blank = True, null = True)
    date=models.DateField(default=datetime.now)

    def getDetails(self):
        data={}
        attributes = self.__dict__
        excluded_attributes = ['_state', 'createdAt']
        for attr_name, attr_value in attributes.items():
            if attr_name not in excluded_attributes:
                data[attr_name]=attr_value
        return data
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

    def getDetails(self):
        data={}
        attributes = self.__dict__
        excluded_attributes = ['_state', 'createdAt']
        for attr_name, attr_value in attributes.items():
            if attr_name not in excluded_attributes:
                data[attr_name]=attr_value
        return data
    
class Additional(models.Model):
    register=models.ForeignKey(Register,on_delete=models.CASCADE,default=1)
    jvd=models.BooleanField(default=False)

    def getDetails(self):
        data={}
        attributes = self.__dict__
        excluded_attributes = ['_state', 'createdAt']
        for attr_name, attr_value in attributes.items():
            if attr_name not in excluded_attributes:
                data[attr_name]=attr_value
        return data