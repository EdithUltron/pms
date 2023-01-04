from django.db import models
from signup.models import FacultyRegister
from datetime import datetime
import logging
import os
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.core.validators import FileExtensionValidator
from django.contrib.contenttypes.fields import GenericRelation


class FacultyEducation(models.Model):
    register=models.ForeignKey(FacultyRegister,on_delete=models.CASCADE,default=1)
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