from django.shortcuts import render

# Create your views here.

def login_blog(resquest):
    return render(resquest,"login.html") 
def signup_blog(resquest):
    return render(resquest,"Sign-up.html") 
