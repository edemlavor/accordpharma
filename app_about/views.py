from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from .forms import MessageForm
from .models import Message

# Create your views here.
# def PageAbout(request):
#    return render(request, 'about/about.html')

def PageAbout(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = MessageForm()
    
    messages = Message.objects.all().order_by('-created_at')
    return render(request, 'about/about.html', {
        'form': form,
        'messages': messages
    })