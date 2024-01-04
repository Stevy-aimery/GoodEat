from my_blog.models import Produit

def run():
    for i in range(8, 14):
        produit = Produit()
        produit.title=(f'Produit N° {i}')
        produit.desc = (f'Description du produit N° {i}')
        produit.image = 'http://default'
        produit.save()
    print("operation reussie !")