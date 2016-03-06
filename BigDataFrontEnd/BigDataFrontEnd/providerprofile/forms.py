from django import forms
from django.utils.translation import ugettext_lazy as _

def get_countries():
    
    country_list = (
    ('1', 'USA'),
    ('2', 'Canada'),
    ('3', 'India'),
    ('4', 'China')
)
    return country_list

def get_languages():
    
    language_list = (
    ('1', 'English'),
    ('2', 'Mandarin'),
    ('3', 'Spanish'),
    ('4', 'Russian')
)
    return language_list

def get_languages_with_none():

    language_list_with_none = (
    ('1', 'None'),
    ('2', 'English'),
    ('3', 'Mandarin'),
    ('4', 'Spanish'),
    ('5', 'Russian')
)
    return language_list_with_none

def get_category_list_with_none():
    category_list_with_none = (
    ('0', 'None'),
    ('1', 'Web Programming'),
    ('2', 'Wordpress'),
    ('3', 'Mobile Dev'),
    ('4', 'Website builders & CMS'),
    ('5', 'UI/UX Design'),
    ('6', 'Convert Files'),
    ('7', 'Ecommerce'),
    ('8', 'User Testing'),
    ('9', 'Quality Assurance'),
    ('10', 'Databases'),
    ('11', 'Desktop App'),
    ('12', 'Data Science'),
    ('13', 'Technical Analysis'),
    ('14', 'IT Support'),
    ('15', 'Network'),
    ('16', 'Security'),
    ('17', 'Systems Administration'),
    ('18', 'Architecture'),
    ('19', 'Cloud'),
    ('20', 'Dev Ops'),
    ('21', 'IT Project Management'),
    ('22', 'Big Data'),
)
    return category_list_with_none

def get_category_list():
    category_list = (
    ('1', 'Web Programming'),
    ('2', 'Wordpress'),
    ('3', 'Mobile Dev'),
    ('4', 'Website builders & CMS'),
    ('5', 'UI/UX Design'),
    ('6', 'Convert Files'),
    ('7', 'Ecommerce'),
    ('8', 'User Testing'),
    ('9', 'Quality Assurance'),
    ('10', 'Databases'),
    ('11', 'Desktop App'),
    ('12', 'Data Science'),
    ('13', 'Technical Analysis'),
    ('14', 'IT Support'),
    ('15', 'Network'),
    ('16', 'Security'),
    ('17', 'Systems Administration'),
    ('18', 'Architecture'),
    ('19', 'Cloud'),
    ('20', 'Dev Ops'),
    ('21', 'IT Project Management'),
    ('22', 'Big Data'),
)
    return category_list

class ProviderEditForm(forms.Form):
    title = forms.CharField(label='Title', label_suffix='',widget=forms.TextInput(attrs={'class':'form-control'}), max_length=100)     
    def __init__(self, *args, **kwargs):
        super(ProviderEditForm, self).__init__(*args, **kwargs)
        self.fields['country'] = forms.ChoiceField(
            choices=get_countries())
        self.fields['language1'] = forms.ChoiceField(
            choices=get_languages())
        self.fields['language2'] = forms.ChoiceField(
            choices=get_languages_with_none())
        self.fields['language3'] = forms.ChoiceField(
            choices=get_languages_with_none())
        self.fields['categories1'] = forms.ChoiceField(
            choices=get_category_list())
        self.fields['categories2'] = forms.ChoiceField(
            choices=get_category_list_with_none())
        self.fields['categories3'] = forms.ChoiceField(
            choices=get_category_list_with_none())
    summary = forms.CharField(label='Summary', label_suffix='',widget=forms.TextInput(attrs={'class':'form-control'}), max_length=300)
    skillsets = forms.CharField(label='Skillsets', label_suffix='',widget=forms.TextInput(attrs={'class':'form-control'}), max_length=300)
   
   

