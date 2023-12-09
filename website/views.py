from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post
from .forms import ContactForm,NewsletterForm

def index_view(request):
    posts=Post.objects.filter(status=1)
    context={'posts': posts}
    return render(request,'website/index.html',context)

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
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
        