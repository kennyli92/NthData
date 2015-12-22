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
    password2 = forms.CharField(label='Confirm Password', label_suffix='',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', label_suffix='',widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label='First name', label_suffix='',widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Last name', label_suffix='',widget=forms.TextInput(attrs={'class':'form-control'}))



    def clean(self):
        errors = []
        if 'password' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                errors.append(_("The two password fields did not match."))

        #if 'email' in self.cleaned_data and 'password2' in self.cleaned_data:
        #    if self.cleaned_data['email'] != self.cleaned_data['password2']:
        #        errors.append(_("Email Test Error!"))

        if errors:
            raise forms.ValidationError(errors)

        return self.cleaned_data


    def clean_username(self):
        data = self.cleaned_data['username']

        try:
            User.objects.get(username=data)
        except User.DoesNotExist:
            return data

        raise forms.ValidationError("This username is not available.")
        return data


    def clean_email(self):
        data = self.cleaned_data['email']

        try:
            User.objects.get(email=data)
        except User.DoesNotExist:
            return data

        raise forms.ValidationError("This email has an account associated. Forgot Username or Password?")
        #add page to recover username or password.
        return data

    

