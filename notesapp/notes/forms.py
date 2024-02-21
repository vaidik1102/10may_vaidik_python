from django import forms
from .models import *
from django.contrib import messages

class signupForm(forms.ModelForm):
    class Meta:
        model=signupForm
        fields='__all__'