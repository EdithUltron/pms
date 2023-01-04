from django.db import models
from django import forms
from .models import Experience,Education,Skills,Projects,Awards,Publications,Scholarships,Activities,Links
from .models import Certificates,Additional

class ExperienceForm(forms.ModelForm):
    class Meta:
        model=Experience
        fields="__all__"
        exclude=["register","cert_count"]
        widgets = {
            'startdate': forms.DateInput(attrs={'type': 'date'}),
            'enddate': forms.DateInput(attrs={'type': 'date'}),
            'company': forms.TextInput(attrs={'placeholder': 'Name of the company'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location of the company'}),
            # 'register': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ExperienceForm, self ).__init__(*args, **kwargs)
        self.fields['certificate'] = forms.FileField(required=False)

    def __str__(self) -> str:
        data={}
        attributes = self.__dict__
        for attr_name, attr_value in attributes.items():
            data[attr_name]=attr_value
        return data
        # return "Experience form"
    
    def clean(self):
        # Get the start and end dates from the form
        start_date = self.cleaned_data.get('startdate')
        end_date = self.cleaned_data.get('enddate')

        # Validate that the start date is not greater than the end date

        if start_date and end_date and start_date >= end_date:
            raise forms.ValidationError("The start date cannot be later than or Equal to the end date.")

        return self.cleaned_data

class CertificatesForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     certificate_name = kwargs.pop('certificate_name', None)
    #     super(CertificatesForm, self).__init__(*args, **kwargs)
    #     self.fields['certificate_name'].initial = certificate_name

    class Meta:
        model=Certificates
        fields = ['certificate_name', 'certificate_file']
    
    # def save(self, commit=True):
    #     # Save the original certificate_file field value
    #     original_certificate_file = self.instance.certificate_file
    #     # Save the updated Certificate object
    #     certificate = super().save(commit=commit)
    #     # If the certificate_file field has changed, delete the previous file
    #     if original_certificate_file and original_certificate_file != certificate.certificate_file:
    #         original_certificate_file.storage.delete(original_certificate_file.name)
    #     return certificate

    # content_type = forms.ModelChoiceField(
    #     queryset=ContentType.objects.all(),
    #     required=False,
    #     widget=forms.HiddenInput()
    # )
    # object_id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    # content_object = GenericForeignKey('content_type', 'object_id')

    # class Meta:
    #     model = Certificate
    #     fields = ['certificate_name', 'certificate_file', 'content_type', 'object_id']

class EducationForm(forms.ModelForm):
    class Meta:
        model=Education
        fields = "__all__" 
        exclude=["register"]
        widgets = {
            'startdate': forms.DateInput(attrs={'type': 'date'}),
            'enddate': forms.DateInput(attrs={'type': 'date'}),
            # 'register': forms.HiddenInput(),
        }   

    def __str__(self) -> str:
        data={}
        attributes = self.__dict__
        for attr_name, attr_value in attributes.items():
            data[attr_name]=attr_value
        return data
    
    def __init__(self, *args, **kwargs):
        super(EducationForm, self ).__init__(*args, **kwargs)
        self.fields['certificate'] = forms.FileField(required=False)

        

class SkillsForm(forms.ModelForm):
    class Meta:
        model=Skills
        fields = "__all__"
        exclude=["register"]

    def __str__(self) -> str:
        data={}
        attributes = self.__dict__
        for attr_name, attr_value in attributes.items():
            data[attr_name]=attr_value
        return data

class ProjectsForm(forms.ModelForm):
    class Meta:
        model=Projects
        fields = "__all__"    
        exclude=["register"]

    def __str__(self) -> str:
        data={}
        attributes = self.__dict__
        for attr_name, attr_value in attributes.items():
            data[attr_name]=attr_value
        return data

class AwardsForm(forms.ModelForm):
    class Meta:
        model=Awards
        fields = "__all__"
        exclude=["register","cert_count"]  

    def __str__(self) -> str:
        data={}
        attributes = self.__dict__
        for attr_name, attr_value in attributes.items():
            data[attr_name]=attr_value
        return data

class PublicationsForm(forms.ModelForm):
    class Meta:
        model=Publications
        fields = "__all__"
        exclude=["register","cert_count"]  
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        } 
    
    def __str__(self) -> str:
        data={}
        attributes = self.__dict__
        for attr_name, attr_value in attributes.items():
            data[attr_name]=attr_value
        return data


class ScholarshipsForm(forms.ModelForm):
    class Meta:
        model=Scholarships
        fields = "__all__"
        exclude=["register","cert_count"]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        } 
    
    def __str__(self) -> str:
        data={}
        attributes = self.__dict__
        for attr_name, attr_value in attributes.items():
            data[attr_name]=attr_value
        return data
    


class ActivitiesForm(forms.ModelForm):
    class Meta:
        model=Activities
        fields = "__all__"
        exclude=["register"]    
    
    def __str__(self) -> str:
        data={}
        attributes = self.__dict__
        for attr_name, attr_value in attributes.items():
            data[attr_name]=attr_value
        return data


class LinksForm(forms.ModelForm):
    class Meta:
        model=Links
        fields = "__all__"
        exclude=["register"] 

    
    def __str__(self) -> str:
        data={}
        attributes = self.__dict__
        for attr_name, attr_value in attributes.items():
            data[attr_name]=attr_value
        return data

class AdditionalForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
    class Meta:
        model=Additional
        fields = "__all__"
        exclude=["register"] 

    
    def __str__(self) -> str:
        data={}
        attributes = self.__dict__
        for attr_name, attr_value in attributes.items():
            data[attr_name]=attr_value
        return data
