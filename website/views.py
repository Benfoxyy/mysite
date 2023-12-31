from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post
from .forms import ContactForm,NewsletterForm
from django.contrib import messages

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt submit')
    form=ContactForm()
    return render(request,'website/contact.html',{'form':form})

def news_view(request):
    if request.method == 'POST':
        form=NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
        