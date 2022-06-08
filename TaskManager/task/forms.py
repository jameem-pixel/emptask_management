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
    title = forms.CharField(widget=TextInput(attrs={'placeholder':'Add new task here..'})) 
    subject = forms.CharField(widget=TextInput(attrs={'placeholder':'Add mail subject here..'})) 
    class Meta:
        model = Taskprovider
        fields = ['employee','priority','title','subject','date','process','requested_by','requested_from']

class Statusform(forms.ModelForm):
    class Meta:
        model = Status_task
        fields = '__all__'

