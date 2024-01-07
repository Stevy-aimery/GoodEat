from django.shortcuts import render
# from django.db.models.functions import Unaccent
from .models import Produit 

def home(resquest):
    list_produits = Produit.objects.all()
    context = {"liste_produits":list_produits} 
    return render(resquest, 'index.html',context)

def detail(resquest, id_produit):
    var_produit = Produit.objects.get(id=id_produit)
    category = var_produit.category
    produit_de_m_category = Produit.objects.filter(category=category)[:6]
    return render(resquest, 'detail.html',{'produit':var_produit,'produit_identique': produit_de_m_category })

def search(resquest):
    query = resquest.GET["produit"]
    list_produits_trouver = Produit.objects.filter(desc__icontains=query)
    return render(resquest, 'search.html', {"list_produits_trouver":list_produits_trouver} )

def userConnecter(resquest):    
    return render(resquest, 'user_connecter.html')
def Apropos(resquest):    
    return render(resquest, 'Apropos.html')  
