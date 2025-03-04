from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
def PageWelcome(request):
    return render(request, 'welcome/welcome.html')