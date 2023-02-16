import genericpath
from django.http import HttpResponse

from typing import Self
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect ,reverse
from . import models
from . serializers import SerilizerCate,SerilizerStock,SerilizerProduit ,SerilizerFournisseur ,SerilizerEntrant, SerilizerUser,SerilizerVente
from rest_framework import generics, response ,decorators , request 
from rest_framework.views import APIView

#--------------------------

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class CategrieCrud(generics.ListCreateAPIView, generics.RetrieveDestroyAPIView,generics.UpdateAPIView):
    queryset=models.Categorie.objects.all()
    serializer_class= SerilizerCate  


class StockCrud(generics.ListCreateAPIView, generics.RetrieveDestroyAPIView,generics.UpdateAPIView):
    queryset=models.Stock.objects.all()
    serializer_class= SerilizerStock      


class ProduitCrud(generics.ListCreateAPIView, generics.RetrieveDestroyAPIView,generics.UpdateAPIView):
    queryset=models.Produit.objects.all()
    serializer_class= SerilizerProduit

class Stockupdate(generics.UpdateAPIView):
    queryset=models.Stock.objects.all()
    serializer_class= SerilizerStock


class FournisseurCrud(generics.ListCreateAPIView, generics.RetrieveDestroyAPIView,generics.UpdateAPIView):
    queryset=models.Fournisseur.objects.all()
    serializer_class= SerilizerFournisseur

class StkEntrantCrud(generics.ListCreateAPIView, generics.RetrieveDestroyAPIView,generics.UpdateAPIView):
    queryset=models.StockEntrant.objects.all()
    serializer_class= SerilizerEntrant


class VenteCrud(generics.ListCreateAPIView, generics.RetrieveDestroyAPIView,generics.UpdateAPIView):
    queryset=models.StockSortant.objects.all()
    serializer_class= SerilizerVente



class UserCrud(generics.ListCreateAPIView, generics.RetrieveDestroyAPIView,generics.UpdateAPIView):
    queryset=models.User.objects.all()
    serializer_class= SerilizerUser

class LoginAPI(APIView):
    def post(self, request,format = None):
        email= request.data.get('email')
        password = request.data.get('password')
        token='h'
        user = models.User.objects.filter(email=email , password= password)
       
        return response.Response({'cv'})


class updatenomproduit(generics.UpdateAPIView):
    queryset=models.Produit.objects.all()
    serializer_class=SerilizerProduit
    def update(self, request, *args, **kwargs):
        instance=self.get_object()
        instance.nom=request.data.get("nom")
        instance.save()
        return Response(SerilizerProduit(instance).data)