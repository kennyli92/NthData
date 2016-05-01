from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from user.models import *
from location.models import *

def get_title(self):
    userObj = User.objects.get(username=self.user)
    try:
        providerObj = Provider.objects.get(user=userObj)
        titleObj = Title.objects.get(provider=providerObj)
        titleTrObj = TitleTr.objects.get(title=titleObj, languageCode='en')
        title = titleTrObj.titleName
    except:
        title = ''
    return title

def get_skillsets(self):
    userObj = User.objects.get(username=self.user)
    skillsets = ''
    try:
        providerObj = Provider.objects.get(user=userObj)
        skillObj = Skill.objects.all().filter(provider=providerObj)
    
        for skill in skillObj:
            skillsets = skillsets + SkillDefTr.objects.get(skillDef=skill.skillDef, languageCode='en').skillName + ', '

        skillsets = skillsets[:-2]
    except:
        return skillsets

    return skillsets

def get_summary(self):
    userObj = User.objects.get(username=self.user)
    try:
        userProfObj = UserProfile.objects.get(user=userObj)
        userProfTrObj = UserProfileTr.objects.get(userProfile=userProfObj)
        summary = userProfTrObj.bioP.strip()
    except:
        summary = ''

    return summary

def get_countries(self):
    userObj = User.objects.get(username=self.user)
    userProfileObj = UserProfile.objects.get(user = userObj)

    try:
        location = Location.objects.get(user = userObj)
        userCountryObj = CountryDefTr.objects.get(countryDef = location.countryDef, languageCode = 'en')
        country_list = ((userCountryObj.id, userCountryObj.country),)
        for countryObj in CountryDefTr.objects.all().filter(languageCode='en'):
            if(userCountryObj.country != countryObj.country):
                country_list = country_list + ((countryObj.id, countryObj.country),)
            else:
                continue
    except:
        country_list = ()
        for countryObj in CountryDefTr.objects.all().filter(languageCode='en'):
            if(countryObj.country == ''):
                country_list = ((countryObj.id, countryObj.country),) + country_list
            else:
                country_list = country_list + ((countryObj.id, countryObj.country),)

    return country_list

#num = user's language priority
def get_languages(self, num):
    userObj = User.objects.get(username=self.user)

    try:
        langObj = Language.objects.get(user=userObj, languageNum=num)
        userLangObj = LanguageDefTr.objects.get(languageDef=langObj.languageDef, languageCode = 'en')
        language_list = ((userLangObj.id, userLangObj.languageName),)
        
        for langDefTrObj in LanguageDefTr.objects.all().filter(languageCode='en'):
            if(userLangObj.languageName != langDefTrObj.languageName):
                language_list = language_list + ((langDefTrObj.id, langDefTrObj.languageName),)
            else:
                continue
    except:
        language_list = ()
        for langDefTrObj in LanguageDefTr.objects.all().filter(languageCode='en'):
            if(langDefTrObj.languageName == ''):
                language_list = ((langDefTrObj.id, langDefTrObj.languageName),) + language_list
            else:
                language_list = language_list + ((langDefTrObj.id, langDefTrObj.languageName),)

    return language_list

# num = user's category priority
def get_categories(self, num):
    userObj = User.objects.get(username=self.user)

    try:
        providerObj = Provider.objects.get(user=userObj)
        catObj = CategoryProvider.objects.get(provider=providerObj, categoryNum=num)
        userCatObj = CategoryDefTr.objects.get(categoryDef=catObj.categoryDef, languageCode='en')
        category_list = ((userCatObj.id, userCatObj.categoryName),)
   
        for catDefTrObj in CategoryDefTr.objects.all().filter(languageCode='en'):
            if(userCatObj.categoryName != catDefTrObj.categoryName):
                category_list = category_list + ((catDefTrObj.id, catDefTrObj.categoryName),)
            else:
                continue
    except:
        category_list = ()
        for catDefTrObj in CategoryDefTr.objects.all().filter(languageCode='en'):
            if(catDefTrObj.categoryName == ''):
                category_list = ((catDefTrObj.id, catDefTrObj.categoryName),) + category_list
            else:
                category_list = category_list + ((catDefTrObj.id, catDefTrObj.categoryName),)

    return category_list


class ProviderEditForm(forms.Form):
    #title = forms.CharField(label='Title', label_suffix='',widget=forms.TextInput(attrs={'class':'form-control'}), max_length=100)     
    def __init__(self, user, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        self.user = user
        super(ProviderEditForm, self).__init__(*args, **kwargs)
        self.fields['title'] = forms.CharField(
            initial=get_title(self),
            label='Title',
            label_suffix='',
            widget=forms.TextInput(attrs={'class':'form-control'}),
            max_length=100)
        self.fields['summary'] = forms.CharField(
            initial=get_summary(self),
            label_suffix='',
            label='Summary', 
            widget=forms.TextInput(attrs={'class':'form-control'}), 
            max_length=300)
        self.fields['skillsets'] = forms.CharField(
            initial=get_skillsets(self),
            label='Skillsets', 
            label_suffix='',
            widget=forms.TextInput(attrs={'class':'form-control'}), 
            max_length=300)
        self.fields['country'] = forms.ChoiceField(
            choices=get_countries(self))
        self.fields['language1'] = forms.ChoiceField(
            choices=get_languages(self, 1))
        self.fields['language2'] = forms.ChoiceField(
            choices=get_languages(self, 2))
        self.fields['language3'] = forms.ChoiceField(
            choices=get_languages(self, 3))
        self.fields['categories1'] = forms.ChoiceField(
            choices=get_categories(self, 1))
        self.fields['categories2'] = forms.ChoiceField(
            choices=get_categories(self, 2))
        self.fields['categories3'] = forms.ChoiceField(
            choices=get_categories(self, 3))
   
   

