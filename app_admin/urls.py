from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('my-produits', user_articles, name="my-produits"),
    path('ajouter-produit', addProduit.as_view(), name="ajouter-produit"),
]