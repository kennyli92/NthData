from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
#class SignUpForm(forms.ModelForm):
#    class Meta:
#        model = User 
#        fields = ['username', 'password', 'email', 'first_name', 'last_name']

class SignUpForm(forms.Form):
    username = forms.CharField(label='Username', label_suffix='',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', label_suffix='',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', label_suffix='',widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label='First name', label_suffix='',widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Last name', label_suffix='',widget=forms.TextInput(attrs={'class':'form-control'}))
