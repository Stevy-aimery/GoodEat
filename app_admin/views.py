from django.shortcuts import render,redirect
from my_blog.models import Produit
from django.contrib.auth.decorators import login_required

# Create your views here.
def dashboard(request):
    return render(request,'db.html')

def user_articles(request):
    if not request.user.is_authenticated:
        return redirect('home')
    list_produits = Produit.objects.filter(user=request.user)
    return render(request, 'my-produits.html', {'liste_produits': list_produits})