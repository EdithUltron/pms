from django import forms
from .models import Experience,Education,Skills,Projects,Awards,Publications,Scholarships,Activities,Links

class ExperienceForm(forms.ModelForm):
    class Meta:
        model=Experience
        fields="__all__"
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
        # return "Experience form"


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
        exclude=["register"]  

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
        exclude=["register"]  
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
        exclude=["register"]
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
