from providerprofile.forms import ProviderEditForm
from django.shortcuts import render, redirect
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
        
        if(skillsetsStr != ''):
            skillsetsList = set(skillsetsStr.split(','))
            curSkillsetCnt = Skill.objects.filter(provider=providerObj).count()
            skillsetsLen = len(skillsetsList)
            skillNum = 1
            #if current skillsets count is greater than passed-in skillsets count, delete 
            #all skills of user above passed-in skillsets count
            if(skillsetsLen < curSkillsetCnt):
                Skill.objects.filter(provider=providerObj, skillNum__gt = skillsetsLen).delete()
            
            for skillset in skillsetsList:
                try:
                    #Find if existing skillset exists in definition table
                    skillDefTrObj = SkillDefTr.objects.get(languageCode = 'en', skillName = skillset.strip())
                except SkillDefTr.DoesNotExist:
                    #Create new skillset definition if it doesn't exist
                    skillDefObj = SkillDef.objects.create()
                    skillDefTrObj = SkillDefTr.objects.create(skillDef = skillDefObj, languageCode='en', skillName = skillset.strip())
                    skillDefTrObj.save()

                skillObj, created = Skill.objects.update_or_create(provider = providerObj, defaults={'skillDef': skillDefTrObj.skillDef}, skillNum = skillNum)
                skillNum += 1
        #if skillset list is empty, delete all skills related to provider
        else:
            Skill.objects.all().filter(provider=providerObj).delete()
        
        # Country
        countryDefTrObj = CountryDefTr.objects.get(id=request.POST['country'], languageCode='en')
        locObj, created = Location.objects.update_or_create(user=userObj, defaults={'countryDef': countryDefTrObj.countryDef})

        # Language 1
        langDefTrObj1 = LanguageDefTr.objects.get(id=request.POST['language1'], languageCode='en')
        langObj1, created = Language.objects.update_or_create(user=userObj, defaults={'languageDef': langDefTrObj1.languageDef}, languageNum=1)      

        # Language 2
        langDefTrObj2 = LanguageDefTr.objects.get(id=request.POST['language2'], languageCode='en')
        langObj2, created = Language.objects.update_or_create(user=userObj, defaults={'languageDef': langDefTrObj2.languageDef}, languageNum=2)
        
        # Language 3
        langDefTrObj3 = LanguageDefTr.objects.get(id=request.POST['language3'], languageCode='en')
        langObj3, created = Language.objects.update_or_create(user=userObj, defaults={'languageDef': langDefTrObj3.languageDef}, languageNum=3)

        # Categories 1
        catDefTrObj1 = CategoryDefTr.objects.get(id=request.POST['categories1'], languageCode='en')
        catObj1, created = CategoryProvider.objects.update_or_create(provider=providerObj, defaults={'categoryDef': catDefTrObj1.categoryDef}, categoryNum = 1)

        # Categories 2
        catDefTrObj2 = CategoryDefTr.objects.get(id=request.POST['categories2'], languageCode='en')
        catObj2, created = CategoryProvider.objects.update_or_create(provider=providerObj, defaults={'categoryDef': catDefTrObj2.categoryDef}, categoryNum = 2)

        # Categories 3
        catDefTrObj3 = CategoryDefTr.objects.get(id=request.POST['categories3'], languageCode='en')
        catObj3, created = CategoryProvider.objects.update_or_create(provider=providerObj, defaults={'categoryDef': catDefTrObj3.categoryDef}, categoryNum = 3)

       # Doesn't recognize whether or not user is logged in because 'request'
       # is not passed on to this page...use render
       # return HttpResponseRedirect('/account/signup/success') # render(request, reverse('registerSuccess'))
        return redirect('/')
    else:
        form = ProviderEditForm(request.user)
        return render(request, 'providerprofile/providerprofile.html', {'form': form})   

def provider_dashboard(request):

     return render(request, 'providerdashboard/pdashboard.html')



    
          
    

