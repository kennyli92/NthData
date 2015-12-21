from signup.forms import SignUpForm
from django.shortcuts import render
from django.views.generic.edit import FormView

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
            lUsername = form.cleaned_data['username']
            lPassword = form.cleaned_data['password']
            lEmail = form.cleaned_data['email']
            lFirst_name = form.cleaned_data['first_name']
            lLast_name = form.cleaned_data['last_name']

            lUser = User.objects.create_user(
            lUsername,
            lPassword,
            lEmail,
            lFirst_name,
            lLast_name
            )

            # redirect to a new URL:
            return HttpResponseRedirect('signup/profile.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()

    return render(request, 'signup/signup.html', {'form': form})