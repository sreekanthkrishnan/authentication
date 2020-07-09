from django.shortcuts import render
from web.forms import UserInfo,UserProfileInfoForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    registered = False

    if request.method =='POST':
        user_form = UserInfo(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile= profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic'in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors or profile_form.errors)
    
    else:
        user_form=UserInfo()
        profile_form=UserProfileInfoForm()
    
    return render(request,'signup.html',{
        'user_form': user_form,
        'profile_form': profile_form,
        'registered':registered
    })

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def login_form(request):
    if request.method =='POST':
        username = request.POST.get(username)
        password = request.POST.get(password)

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
                
            else:
                return HttpResponse('Account is not valid')
        else:
            return HttpResponse('invalid username or password')
        
    else:
        return render(request,'login.html',{'login_form':login_form})