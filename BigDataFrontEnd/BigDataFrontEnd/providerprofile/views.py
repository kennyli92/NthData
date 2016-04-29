from providerprofile.forms import ProviderEditForm
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from user.models import *
from location.models import *
from django.core.urlresolvers import reverse


def provider_profile(request):

    if (request.method == 'POST') and ('providerProfileUpdate' in request.POST):

        postExtractedUsername = request.POST['username']

        # Get the user object based on the extracted username
        userObj = get_object_or_404(User, username=postExtractedUsername) 
        providerObj, created = Provider.objects.get_or_create(user=userObj)  
  
        # Title          
        titleObj, created = Title.objects.get_or_create(provider=providerObj)
        titleTrObj, created = TitleTr.objects.update_or_create(title=titleObj, defaults={'titleName': request.POST['title']}, languageCode='en')

        # Summary
        userProf, created = UserProfile.objects.get_or_create(user=userObj)
        userProfTr, created = UserProfileTr.objects.update_or_create(userProfile=userProf, defaults={'bioP': request.POST['summary']})

        # Skillset
        skillsetsStr = request.POST['skillsets']
        skillsetsList = skillsetsStr.split(',')
        for skillset in skillsetsList:
            try:
                skillDefTrObj = SkillDefTr.objects.get(languageCode = 'en', skillName = skillset.strip())
                skillDefObj = skillDefTrObj.skillDef
            except SkillDefTr.DoesNotExist:
                skillDefObj = SkillDef.objects.create()
                skillDefTrObj = SkillDefTr.objects.create(skillDef = skillDefObj, languageCode='en', skillName = skillset.strip())
                skillDefTrObj.save()

            skillObj = Skill(provider = providerObj, skillDef = skillDefObj)
            skillObj.save()
        
        # Country
        try:
            countryDefTrObj = CountryDefTr.objects.get(country=request.POST['country'])
            locObj, created = Location.objects.update_or_create(user=userObj, defaults={'countryDef': countryDefTrObj.countryDef})
        # empty country entry for user if choice = blank
        except:
            pass

        # Language 1
        try:
            langDefTrObj = LanguageDefTr.objects.get(languageName=request.POST['language1'])
            langObj, created = Language.objects.update_or_create(user=userObj, defaults={'languageDef': langDefTrObj.languageDef, 'languageNum': 1})
        # empty language 1 entry for user if choice = blank
        except:
            pass

        # Language 2
        try:
            langDefTrObj = LanguageDefTr.objects.get(languageName=request.POST['language2'])
            langObj, created = Language.objects.update_or_create(user=userObj, defaults={'languageDef': langDefTrObj.languageDef, 'languageNum': 2})
        # empty language 2 entry for user if choice = blank
        except:
            pass

        # Language 3
        try:
            langDefTrObj = LanguageDefTr.objects.get(languageName=request.POST['language3'])
            langObj, created = Language.objects.update_or_create(user=userObj, defaults={'languageDef': langDefTrObj.languageDef, 'languageNum': 3})
        # empty language 3 entry for user if choice = blank
        except:
            pass

        # Categories 1
        try:
            catDefTrObj = CategoryDefTr.objects.get(categoryName=request.POST['categories1'])
            catObj, created = CategoryProvider.objects.update_or_create(provider=providerObj, defaults={'categoryDef': catDefTrObj.categoryDef, 'categoryNum': 1})
        # empty categories 1 entry for user if choice = blank
        except:
            pass

        # Categories 2
        try:
            catDefTrObj = CategoryDefTr.objects.get(categoryName=request.POST['categories2'])
            catObj, created = CategoryProvider.objects.update_or_create(provider=providerObj, defaults={'categoryDef': catDefTrObj.categoryDef, 'categoryNum': 2})
        # empty categories 2 entry for user if choice = blank
        except:
            pass

        # Categories 3
        try:
            catDefTrObj = CategoryDefTr.objects.get(categoryName=request.POST['categories3'])
            catObj, created = CategoryProvider.objects.update_or_create(provider=providerObj, defaults={'categoryDef': catDefTrObj.categoryDef, 'categoryNum': 3})
        # empty categories 3 entry for user if choice = blank
        except:
            pass

       # Doesn't recognize whether or not user is logged in because 'request' is not passed on to this page...use render
        return HttpResponseRedirect('/account/signup/success') # render(request, reverse('registerSuccess'))
    else:
        form = ProviderEditForm(request.user)
        return render(request, 'providerprofile/providerprofile.html', {'form': form})   

def provider_dashboard(request):

     return render(request, 'providerdashboard/pdashboard.html')



    
          
    

