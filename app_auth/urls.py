from django.urls import path
from .views import login_blog,signup_blog,logout_blog

urlpatterns = [
    path("login", login_blog, name="login-blog"),
    path("enregistrer", signup_blog, name="signup-blog"),
    path("logout", logout_blog, name="logout-blog")
]
# authentification/login  