"""
URL configuration for Global_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Station_Essence.views import dash_essens,navbar,entete,dash,mairie,livraison,essence, logout_user


urlpatterns = [

    #logout
    path('logout/',logout_user,name='logout'),
    
    #les pages de tableau de bord général et celui de l'essence
    path('Dashboard_Essence/',dash_essens,name="dash"),
    path('dash/',dash,name="dashs"),
    
    #les parties du tableau de bord
    path('Bar/',navbar,name='navbar'),
    path('entete/',entete,name='entete'),
    
    


   
    #l'url de la mairie
    
    path('Mairie/',mairie,name='mairie'),
    
      #l'url de la livraison
    
    path('livraison/',livraison,name='livraison'),
    
    path('essence/',essence,name='essence'),
   
]
