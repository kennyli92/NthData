﻿from signup.forms import SignUpForm
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from  django.contrib.auth.views import password_reset, password_reset_confirm
from django.core.urlresolvers import reverse

#def register(request):
#    form = SignUpForm()
#    return render(request, 'signup/signup.html', {'form': form})

def account(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required           
            user = User.objects.create_user(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password'],
            email = form.cleaned_data['email'],
            first_name = form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name']
            )

            
            # add to 'user' group
            group = Group.objects.get(name='user')
            user.groups.add(group)

            # redirect to a new URL:
            return HttpResponseRedirect('signup/success')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()

    return render(request, 'signup/signup.html', {'form': form})

def register_success(request):
    return render_to_response(
    'signup/profile.html',
    )

def password_recover(request):
    return password_reset(request, template_name='recovery/passwordrecovery.html', email_template_name='recovery/password_reset_email.html',
                          subject_template_name='recovery/password_reset_subject.txt', post_reset_redirect=reverse('password_recover_email_sent'))
def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='recovery/passwordrecovery.html',
        uidb64=uidb64, token=token, post_reset_redirect='signup/signup.html')
def password_recover_email_sent(request):
     return render_to_response(
    'recovery/email_sent.html',
    )