from django import forms
from .facultymodels import FacultyEducation

class EducationForm(forms.ModelForm):
    class Meta:
        model=FacultyEducation
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