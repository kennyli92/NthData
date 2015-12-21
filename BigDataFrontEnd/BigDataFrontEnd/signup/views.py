from signup.forms import SignUpForm
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

#def register(request):
#    form = SignUpForm()
#    return render(request, 'signup/signup.html', {'form': form})

def register(request):
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