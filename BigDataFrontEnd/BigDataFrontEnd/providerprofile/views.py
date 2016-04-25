﻿from providerprofile.forms import ProviderEditForm
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from user.models import UserProfile, Provider, Title, TitleTr, UserProfileTr, Skill, SkillDef, SkillDefTr
from location.models import CountryDef, CountryDefTr, Location
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
        countryDefTr = CountryDefTr.objects.get(countryDef=request.POST['country'])
        countryDefObj  = CountryDef.objects.get(id=countryDefTr.countryDef.id)
        locObj, created = Location.objects.update_or_create(user=userObj, defaults={'countryDef': countryDefObj})


       # locObj, created = Location.objects.update_or_create(user=userObj, countryDef=countryDefObj)
        
       # Doesn't recognize whether or not user is logged in because 'request' is not passed on to this page...use render
        return HttpResponseRedirect('/account/signup/success') # render(request, reverse('registerSuccess'))
    else:
        form = ProviderEditForm(request.user)
        return render(request, 'providerprofile/providerprofile.html', {'form': form})   

def provider_dashboard(request):

     return render(request, 'providerdashboard/pdashboard.html')



    
          
    

