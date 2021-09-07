from django.http import request
from django.shortcuts import render, redirect
# login, auth and logout method for django default user database
from django.contrib.auth import login, authenticate, logout
# decorator for login required 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

# importing django auto register and login form.
#from django.contrib.auth.forms import UserCreationForm
# importing custom form.py created for user creation 
from .forms import CustomUserCreationForm

#flash messages to be displayed once
from django.contrib import messages

# Create your views here.


def loginUser(request):
    page = 'login'
    context = {'page': page}
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request,'Username/Password is incorrect')

    return render(request, 'users/login_register.html', context)

def logoutUser(request):
    logout(request)
    messages.error(request,'Username successfully logged out')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account is created')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'error while registration')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context) 

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    # skills that have a description
    topSkills = profile.skill_set.exclude(description__exact="")

    # skills that don't have a description 
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'topSkills':topSkills, 'otherSkills':otherSkills}
    return render(request, 'users/user-profile.html', context) 

