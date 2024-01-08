from django.shortcuts import render
from my_blog.models import Produit
from django.contrib.auth.decorators import login_required

# Create your views here.
def dashboard(request):
    return render(request,'db.html')

# @login_required
def user_articles(request):
    list_produits = Produit.objects.filter(user=request.user)
    return render(request, 'my-produits.html', {'liste_produits': list_produits})