from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.

def login_blog(request):
    if request.method == "POST":
        username = request.POST["username"]
        pwd = request.POST["pwd"]
        user = authenticate(username=username, password=pwd)
        if user is not None:
            return redirect("home")
            # return redirect("Sign-up.html Apropos")
        else:
            messages.error(request,"Erreur d'authentification")
            return render(request,"login.html")
            # message.error(request,"echec de la connexion")
        
        
    return render(request,"login.html")


def signup_blog(request):
    return render(request,"Sign-up.html") 
