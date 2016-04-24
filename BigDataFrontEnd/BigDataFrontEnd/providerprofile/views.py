from providerprofile.forms import ProviderEditForm
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from user.models import UserProfile, Provider, Title, TitleTr, UserProfileTr, Skill, SkillDef, SkillDefTr
from location.models import CountryDef, CountryDefTr, Location


def provider_profile(request):

    if (request.method == 'POST') and ('providerProfileUpdate' in request.POST):

        postExtractedUsername = request.POST['username']

        # Get the user object based on the extracted username
        userObj = get_object_or_404(User, username=postExtractedUsername) 
        providerObj, created = Provider.objects.get_or_create(user=userObj)  
  
        # Title          
        titleObj, created = Title.objects.get_or_create(provider=providerObj)
        titleTrObj = TitleTr.objects.create(title=titleObj, titleName=request.POST['title'])

        # Summary
        userProf, created = UserProfile.objects.get_or_create(user=userObj)
        userProfTr, created = UserProfileTr.objects.get_or_create(userProfile=userProf, bioP=request.POST['summary'])
        userProfTr.save();

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

        #

        return HttpResponseRedirect('/account/signup/success')
    else:
        form = ProviderEditForm(request.user)
        return render(request, 'providerprofile/providerprofile.html', {'form': form})   

def provider_dashboard(request):

     return render(request, 'providerdashboard/pdashboard.html')



    
          
    

