"""Gestion_Stock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Stock_Management import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Categorie/<int:pk>',views.CategrieCrud.as_view(),name='Categorie'),
    path('Categorie/',views.CategrieCrud.as_view(),name='Categorie'),
    path('Stock/<int:pk>/',views.StockCrud.as_view(),name='Stock'),
    path('Stock/',views.StockCrud.as_view(),name='Stock'),
    path('Produit/<int:pk>/',views.ProduitCrud.as_view(),name='Produit'),
    path('Produit/',views.ProduitCrud.as_view(),name='Produit'),
    path('Fournisseur/<int:pk>/',views.FournisseurCrud.as_view(),name='Fournissuer'),
    path('Fournisseur/',views.FournisseurCrud.as_view(),name='Fournissuer'),
    path('Stock_Entrant/<int:pk>/',views.StkEntrantCrud.as_view(),name='Stock Entrant'),
    path('Stock_Entrant/',views.StkEntrantCrud.as_view(),name='Stock Entrant'),
    path('Vente/<int:pk>/',views.VenteCrud.as_view(),name='Vente'),
    path('Vente/',views.VenteCrud.as_view(),name='Vente'),
    path('Users/<int:pk>/',views.UserCrud.as_view(),name='Users'),
    path('Users/',views.UserCrud.as_view(),name='Users'),
    path('up/<int:pk>/',views.Stockupdate.as_view(),name='up'),
    path('Login/',views.LoginAPI.as_view(),name='Login'),



]
