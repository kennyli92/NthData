from django import forms
from django.utils.translation import ugettext_lazy as _

def get_countries():
    
    choices_list = (
    ('1', 'USA'),
    ('2', 'Canada'),
    ('3', 'India'),
    ('4', 'China')
)

    return choices_list


class ProviderEditForm(forms.Form):
    title = forms.CharField(label='Title', label_suffix='',widget=forms.TextInput(attrs={'class':'form-control'}), max_length=100)   
    def __init__(self, *args, **kwargs):
        super(ProviderEditForm, self).__init__(*args, **kwargs)
        self.fields['country'] = forms.ChoiceField(
            choices=get_countries())

