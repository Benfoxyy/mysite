from django.shortcuts import render

def login_view(request):
    if request.user.is_authenticated:
        msg=f'{request.user.username} is logged in before!'
    else:
        msg='is not logged in!'
    return render(request,'accounts/login.html',{'msg':msg})

def logout_view(request):
    return render(request,'accounts/logout.html')

def signup_view(request):
    return render(request,'accounts/signup.html')