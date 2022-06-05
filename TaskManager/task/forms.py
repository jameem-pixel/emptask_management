from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, fields
from django import forms
from django.forms.widgets import TextInput

from . models import *
class Userform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']


class TitleForm(forms.ModelForm):
    name = forms.CharField(widget=TextInput(attrs={'placeholder':'Add new task here..'})) 
    class Meta:
        model = Employee
        fields = ['title','subject']

