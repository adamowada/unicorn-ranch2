from django import forms

class InputForm(forms.Form):
    name = forms.CharField(max_length=200)
    color = forms.CharField(max_length=200)
    location = forms.CharField(max_length=200)
