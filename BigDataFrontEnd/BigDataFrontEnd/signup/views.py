from .forms import SignUpForm
from django.shortcuts import render
from django.views.generic.edit import FormView

#class Register(FormView):
#    template_name = 'signup/signup.html'
#    form_class = SignUpForm

def register(request):
    form = SignUpForm()

    return render(request, 'signup/signup.html', {'form': form})
