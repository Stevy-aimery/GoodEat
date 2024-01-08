from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('my-produits', user_articles, name="my-produits"),
]