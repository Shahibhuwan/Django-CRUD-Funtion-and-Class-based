from django import forms
from . models import Student


#from django import forms
#class GeeksForm(forms.Form):
#    title = forms.CharField()
#    pub_date = forms.DateField()  from django formset

class StudentForm(forms.ModelForm):
    
    class Meta:
        model =  Student
        fields = "__all__"       #exclude = ['title'] , fields name can be used explicityly 
        labels = {'name' : 'Enter Name', 'email' : 'Enter Email', 'password' : 'Enter password'}
        error_messages = {'name': {'required ': 'Name likhna jaruri cha'}, 'email': {'required ': 'Email lekhna jaruri cha'}, 'password': {'required': 'Password lekhna jaruri cha'}}

        widgets = {'password': forms.PasswordInput(),}  #{'name': forms.TextInput(attrs= {'class': 'myclass ', 'placeholder':'Yaha name lekhne'})}
