from django.shortcuts import render,redirect
from django.views.generic.edit  import CreateView, UpdateView, DeleteView
from my_blog.models import Produit
from my_blog.forms import ArticleForm
# from django.contrib.auth.decorators import login_required

# Create your views here.
def dashboard(request):
    return render(request,'db.html')

def user_articles(request):
    if not request.user.is_authenticated:
        return redirect('home')
    list_produits = Produit.objects.filter(user=request.user)
    return render(request, 'my-produits.html', {'liste_produits': list_produits})

# Vu fondé sur les classs Django

class addProduit(CreateView):
    model = Produit
    form_class = ArticleForm
    template_name = "add-produit.html"
    succes_url = "my-produits"
