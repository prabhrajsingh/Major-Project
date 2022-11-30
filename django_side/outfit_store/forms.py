# forms.py
from django import forms
from .models import *

class DressForm(forms.ModelForm):  
    class Meta:
        model = outfit_upload
        fields = ['User_name', 'dress_name', 'dress']