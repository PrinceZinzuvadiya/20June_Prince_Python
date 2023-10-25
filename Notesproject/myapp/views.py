from django.shortcuts import render, redirect
from .forms import signupform
from django.contrib import messages
from .models import *

def index(request):
    if request.method=='POST':
        if request.POST.get('signup')=='signup': #root condition
            newuser=signupform(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Signup succesful")
                messages.success(request, 'signup succcess')
            else:
                print(newuser.errors)
                messages.error(request, 'error')
        elif request.POST.get('signin')=='signin':
            unm=request.POST['username']
            pas=request.POST['password']

            user=usersignup.objects.filter(username=unm, password=pas)
            if user:
                print("Login succesful")
                messages.success(request, 'login success')
                request.session['user']=unm
                return redirect ('notes')
        else:
            messages.error(request, 'Login fail')
    return render (request, 'index.html')

def notes(request):
    user=request.session.get('user')
    return render (request, 'notes.html', {'user':user})

def about(request):
    return render (request, 'about.html')

def contact(request):
    return render (request, 'contact.html')

def profile(request):
    return render (request, 'profile.html')