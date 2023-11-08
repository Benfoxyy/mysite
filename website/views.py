from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about_us.html')

def contact(request):
    return render(request,'website/contact.html')