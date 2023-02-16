from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(models.Model):
    nom = models.CharField(max_length=100)
    prenom =models.CharField(max_length=100)
    email = models.EmailField()
    numeroTel =models.IntegerField( )
    password=models.CharField(max_length=10)

    def __str__ (self) :
        return self.nom

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    numeroTel =models.IntegerField( )

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__ (self) :
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=100,)
    categorie=models.ForeignKey(Categorie, on_delete=models.CASCADE)
    

    def __str__ (self) :
        return self.nom


class Stock(models.Model):
    produits = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=0 )
    prix = models.FloatField(default=0.0)
    def __str__ (self) :
        return self.produits

     

class StockEntrant(models.Model):
    fournisseur=models.ForeignKey(Fournisseur, on_delete=models.CASCADE)   
    produits=models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField( )
    prix=models.FloatField()
    date = models.DateField(auto_now_add=True)
    # user=models.ForeignKey(User, on_delete=models.CASCADE)


class StockSortant(models.Model):
    produits=models.ForeignKey(Produit,on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prix=models.FloatField()
    date = models.DateField(auto_now_add=True)
    # user=models.ForeignKey(User, on_delete=models.CASCADE)