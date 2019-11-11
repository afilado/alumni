from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.

def my_home(request):
    return render(request, 'MyApp/home.html')

