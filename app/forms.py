from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from app.models import Ert




class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2',)
        
        
        



class ErtForm(forms.ModelForm):
	class Meta:
		model=Ert
		fields='__all__'