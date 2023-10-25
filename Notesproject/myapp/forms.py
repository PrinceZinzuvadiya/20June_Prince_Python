from django import forms
from .models import *

class signupform(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'