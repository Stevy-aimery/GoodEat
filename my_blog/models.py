from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
 
class Produit(models.Model):
    # models.CharField : Chaine de caratere = varchar
    
    title = models.CharField(max_length = 60)
    desc = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "", null=True,blank=True)
    created_add = models.DateTimeField(auto_now_add=True)
    update_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
