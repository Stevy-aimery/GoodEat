from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *

# Create your views here.

def login_blog(request):
   if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = authenticate(username=username, password=pwd)
            if user is not None:
                login(request,user) # fonction qui stock l'utilsateur dans l'object request
                return redirect("user_connecter")
                # context = {'user': request.user}
                # return render(request, 'user_connecter.html', context)
            else:
                messages.error(request,"Echec d'authentification")
                return render(request,"login.html",{"form":form})
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += 'is-invalid'
            return render(request,"login.html",{"form":form})

   else:
        form = LoginForm()
        return render(request,"login.html",{"form":form})


def signup_blog(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            # comfirmPwd  = form.cleaned_data['comfirmPwd']
            user = User.objects.create_user(username=username, password=pwd)
            if user is not None:
                return redirect("login-blog")
            else:
                messages.error(request,"Echec de la création du compte")
                return render(request,"Sign-up.html",{"form":form})
        else:
            return render(request,"Sign-up.html",{"form":form}) 

    form = SignupForm()
    return render(request,"Sign-up.html",{"form":form})

def logout_blog(request):
    logout(request)
    return redirect('home')
        
