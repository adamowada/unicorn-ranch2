from django import forms
from .models import Unicorn

class InputForm(forms.ModelForm):
    class Meta:
        model = Unicorn
        fields = '__all__'
