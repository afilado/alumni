from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from webapp.forms import SignUpForm

# Create your views here.


def my_home(request):
    return render(request, 'MyApp/home.html')


@login_required


def logout(request):
    return render(request, 'MyApp/logout.html')


def registration_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user = form.save(commit=True)
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('account/login')
    return render(request, 'MyApp/registration.html', {'form': form})

