from django import forms

class outfit_upload_form(forms.Form):
    name = forms.CharField()
    dress = forms.ImageField()