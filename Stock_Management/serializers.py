from rest_framework.serializers import ModelSerializer 
from . import models

class SerilizerUser(ModelSerializer):
    class Meta:
        model = models.User
        fields= '__all__'

class SerilizerCate(ModelSerializer):
    class Meta:
        model = models.Categorie
        fields= '__all__'

class SerilizerStock(ModelSerializer):
    class Meta:
        model = models.Stock
        fields= '__all__'   

class SerilizerProduit(ModelSerializer):
    class Meta:
        model = models.Produit
        fields= '__all__'  


class SerilizerFournisseur(ModelSerializer):
    class Meta:
        model = models.Fournisseur
        fields= '__all__'  

class SerilizerEntrant(ModelSerializer):
    class Meta:
        model = models.StockEntrant
        fields= '__all__'  

class SerilizerVente(ModelSerializer):
    class Meta:
        model = models.StockSortant
        fields= '__all__'  

 