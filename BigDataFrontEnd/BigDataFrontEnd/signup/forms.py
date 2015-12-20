from django import forms
from django.contrib.auth.models import User

#class SignUpForm(forms.ModelForm):
#    class Meta:
#        model = User 
#        fields = ['username', 'password', 'email', 'first_name', 'last_name']

class SignUpForm(forms.Form):
    username = forms.CharField()
    password = forms.PasswordInput()
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
