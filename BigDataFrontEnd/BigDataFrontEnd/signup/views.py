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
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            user = User.objects.create_user(
            username,
            password,
            email,
            first_name,
            last_name
            )
            # redirect to a new URL:
            return HttpResponseRedirect('signup/profile.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()

    return render(request, 'signup/signup.html', {'form': form})